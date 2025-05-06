# SHL Assessment Recommendation System

## 🚀 Submission URLs

1. **Demo URL** (Streamlit UI): [your-streamlit-url]
2. **API Endpoint URL**: [your-render-api-url]/recommend
3. **GitHub URL**: [your-github-repo-url]

---

## 🛠️ Deployment Instructions

### 1. Deploy FastAPI API on Render.com
- Sign up at [https://render.com/](https://render.com/)
- Connect your GitHub repo
- Render will auto-detect `render.yaml` and deploy the API
- After deployment, your `/recommend` endpoint will be at `https://your-render-service.onrender.com/recommend`

### 2. Deploy Streamlit UI on Streamlit Community Cloud
- Sign up at [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Click 'New app' and select your repo and `app/ui.py` as the entry point
- Set `API_URL` in Streamlit secrets to your deployed Render API endpoint
- Your demo will be live at `https://your-app.streamlit.app/`

---

## 📝 Approach
See `approach.md` for a summary of the technical approach, tools, and evaluation.

---

## 🧪 Evaluation
Run `python3 evaluate.py` to compute Mean Recall@3 and MAP@3 with the provided test queries.

---

## 💻 Local Development
- Install dependencies: `pip install -r requirements.txt`
- Run API: `uvicorn app.api:app --reload`
- Run UI: `streamlit run app/ui.py`

## Overview
This project provides a web-based recommendation engine for SHL assessments, allowing hiring managers to input a job description or query and receive the most relevant SHL assessment recommendations.

## Features
- **API Endpoints:**
  - `/health`: Health check endpoint
  - `/recommend`: Returns up to 10 relevant SHL assessments for a given query or job description
- **Web UI:** Simple interface to submit queries and view recommendations
- **Evaluation:** Scripts to compute MAP@3 and Mean Recall@3 on a provided test set

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit
- **NLP:** Sentence Transformers for semantic search
- **Data:** SHL assessment catalog (parsed from shl.com)

## Setup
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the API: `uvicorn app.api:app --reload`
4. Run the UI: `streamlit run app/ui.py`

## Directory Structure
- `app/` - API and UI code
- `data/` - Assessment catalog and embeddings
- `evaluation/` - Evaluation scripts and test sets

## Usage
- Submit a query or job description via the UI or `/recommend` endpoint to get recommendations.

## Evaluation
- Run `python evaluation/evaluate.py` to compute MAP@3 and Mean Recall@3.

## License
MIT
