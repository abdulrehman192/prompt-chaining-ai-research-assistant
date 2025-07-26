# retriever.py
import requests

def search_web(query: str) -> str:
    # A simple Wikipedia search as a placeholder
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No information found.")
    return "No information found."
