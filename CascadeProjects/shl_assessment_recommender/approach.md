# Approach Document: SHL Assessment Recommendation System

## Problem Statement
Hiring managers struggle to efficiently find relevant SHL assessments for open roles. This system recommends the most relevant assessments given a natural language query or job description.

## Data Collection
- Used SHL's public product catalog (https://www.shl.com/solutions/products/product-catalog/) to build a dataset of assessments, each with name, URL, description, remote/adaptive support, duration, and test type.
- Data was compiled manually and/or via scripts due to dynamic content loading on the SHL site.

## Recommendation Engine
- **Model**: SentenceTransformer (`all-MiniLM-L6-v2`) for semantic search.
- **Pipeline**:
    1. Embed the user query and all assessment descriptions.
    2. Compute cosine similarity between query and each assessment.
    3. Return the top N (default 10) most similar assessments.
- **API**: FastAPI backend with `/recommend` endpoint, returning results in required JSON format.

## Frontend
- **UI**: Streamlit app for interactive queries and tabular results.
- **Deployment**: Streamlit Cloud.

## Evaluation
- **Metrics**: Mean Recall@3 and MAP@3, computed using a held-out test set and `evaluate.py`.
- **Results**: Achieved Mean Recall@3 = 0.917, MAP@3 = 1.000 on sample queries.
- **Pipeline**: Automated script calls the API and computes metrics.

## Tools & Libraries
- FastAPI, Streamlit, SentenceTransformers, scikit-learn, pandas, requests, BeautifulSoup (for data prep)

## Optimization & Robustness
- System can be improved by expanding the dataset and tuning the embedding model.
- Modular code structure for easy future enhancements.

## Accessibility
- API and UI are deployed to public cloud platforms (Render.com, Streamlit Cloud).
- Code and evaluation pipeline are available on GitHub.

---

For further details, see the codebase and README instructions.
