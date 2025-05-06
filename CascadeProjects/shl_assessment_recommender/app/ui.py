import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

API_URL = st.secrets.get("API_URL", "http://localhost:8000/recommend")

query = st.text_area("Enter job description, query, or paste a JD URL:")
if st.button("Get Recommendations"):
    with st.spinner("Fetching recommendations..."):
        resp = requests.post(API_URL, json={"query": query})
        if resp.status_code == 200:
            data = resp.json()
            if data["recommendations"]:
                st.write("### Recommendations")
                st.table([
                    {
                        "Assessment Name": f"[{r['name']}]({r['url']})",
                        "Remote Testing": r['remote_testing_support'],
                        "Adaptive/IRT": r['adaptive_irt_support'],
                        "Duration": r['duration'],
                        "Test Type": r['test_type']
                    }
                    for r in data["recommendations"]
                ])
            else:
                st.warning("No recommendations found.")
        else:
            st.error(f"API error: {resp.status_code}")
