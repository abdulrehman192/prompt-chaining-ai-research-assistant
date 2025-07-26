# prompts.py
def question_decomposer_prompt(main_question: str) -> str:
    return f"""
    You are an expert researcher. Break down the following research question
    into 3-5 smaller sub-questions for detailed analysis:
    Question: "{main_question}"
    Return only the list of sub-questions.
    """

def summarization_prompt(sub_question: str, context: str) -> str:
    return f"""
    Summarize the following information to answer this sub-question:
    Sub-question: {sub_question}
    Context: {context}
    Answer in 3-4 concise sentences.
    """

def synthesis_prompt(main_question: str, sub_answers: str) -> str:
    return f"""
    You are an AI research assistant. Using the answers to sub-questions below,
    synthesize a detailed, coherent, and well-structured final report
    that addresses the main question:
    Main Question: {main_question}
    Sub-answers: {sub_answers}
    """
