from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

app = FastAPI()

# Dummy data path (to be replaced with actual path)
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/assessments.json')

# Load model and data (this is a stub, real implementation will load actual data and embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

class RecommendRequest(BaseModel):
    query: str
    top_k: int = 10

class Assessment(BaseModel):
    name: str
    url: str
    remote_testing_support: str
    adaptive_irt_support: str
    duration: str
    test_type: str

class RecommendResponse(BaseModel):
    recommendations: List[Assessment]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend", response_model=RecommendResponse)
def recommend(req: RecommendRequest):
    # Load data
    if not os.path.exists(DATA_PATH):
        raise HTTPException(status_code=500, detail="Assessment data not found.")
    with open(DATA_PATH, 'r') as f:
        assessments = json.load(f)
    # Embed query
    query_emb = model.encode([req.query])
    # Embed assessment descriptions
    descs = [a['description'] for a in assessments]
    emb_matrix = model.encode(descs)
    # Compute similarity
    sims = cosine_similarity(query_emb, emb_matrix)[0]
    top_idx = sims.argsort()[::-1][:req.top_k]
    results = []
    for idx in top_idx:
        a = assessments[idx]
        results.append(Assessment(
            name=a['name'],
            url=a['url'],
            remote_testing_support=a['remote_testing_support'],
            adaptive_irt_support=a['adaptive_irt_support'],
            duration=a['duration'],
            test_type=a['test_type']
        ))
    return RecommendResponse(recommendations=results)
