import requests
import json

def recall_at_k(relevant, predicted, k):
    relevant_set = set(relevant)
    pred_set = set(predicted[:k])
    return len(relevant_set & pred_set) / len(relevant_set) if relevant_set else 0

def average_precision_at_k(relevant, predicted, k):
    score = 0.0
    num_hits = 0.0
    for i, p in enumerate(predicted[:k]):
        if p in relevant:
            num_hits += 1
            score += num_hits / (i + 1)
    return score / min(len(relevant), k) if relevant else 0

def evaluate(test_queries, api_url, k=3):
    recalls = []
    maps = []
    for q in test_queries:
        query = q['query']
        relevant = q['relevant']
        resp = requests.post(api_url, json={'query': query, 'top_k': k})
        if resp.status_code != 200:
            print(f"API error for query: {query}")
            continue
        recs = resp.json()['recommendations']
        predicted = [r['name'] for r in recs]
        recalls.append(recall_at_k(relevant, predicted, k))
        maps.append(average_precision_at_k(relevant, predicted, k))
    mean_recall = sum(recalls) / len(recalls)
    mean_ap = sum(maps) / len(maps)
    print(f"Mean Recall@{k}: {mean_recall:.3f}")
    print(f"MAP@{k}: {mean_ap:.3f}")

if __name__ == "__main__":
    # Example test set (add more as needed)
    test_queries = [
        {
            "query": "I am hiring for Java developers who can also collaborate effectively with my business teams. Looking for an assessment(s) that can be completed in 40 minutes.",
            "relevant": [
                "Core Java (Entry Level) (New)",
                "Java 8 (New)",
                "Automata - Fix (New)",
                "Agile Software Development"
            ]
        },
        {
            "query": "Assessment for manual software testing skills, test case design, and QA knowledge.",
            "relevant": [
                "Manual Testing (New)",
                "Automata Selenium"
            ]
        },
        {
            "query": "I want to hire new graduates for a sales role in my company, the budget is for about an hour for each test. Give me some options",
            "relevant": [
                "Entry Level Sales Solution"
            ]
        }
    ]
    api_url = "http://localhost:8000/recommend"
    evaluate(test_queries, api_url, k=3)
