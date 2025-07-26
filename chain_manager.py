# chain_manager.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import question_decomposer_prompt, synthesis_prompt
from retriever import search_web
from summarizer import summarize_text

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str) -> str:
    """
    Call the LLM with a given prompt.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

def run_chain(main_question: str) -> str:
    # Step 1: Decompose the main question
    sub_questions = call_llm(question_decomposer_prompt(main_question)).split("\n")
    sub_answers = []

    # Step 2: For each sub-question, retrieve info and summarize
    for sub_q in sub_questions:
        sub_q = sub_q.strip("- ").strip()
        if sub_q:
            context = search_web(sub_q)
            answer = summarize_text(sub_q, context)
            sub_answers.append(f"{sub_q}: {answer}")

    # Step 3: Synthesize final report
    final_report = call_llm(synthesis_prompt(main_question, "\n".join(sub_answers)))
    return final_report
