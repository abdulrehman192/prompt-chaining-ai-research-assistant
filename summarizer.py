# summarizer.py
from openai import OpenAI
from prompts import summarization_prompt
import os
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(sub_question: str, context: str) -> str:
    """
    Summarizes the context to answer the sub-question concisely.
    """
    prompt = summarization_prompt(sub_question, context)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert summarizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
