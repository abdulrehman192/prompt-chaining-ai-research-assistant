# main.py
from chain_manager import run_chain
import gradio as gr

def chat_interface(question, history=[]):
    report = run_chain(question)
    return report

if __name__ == "__main__":
    gr.ChatInterface(
    fn=chat_interface,
    title="🤖 AI Research Assistant",
    description="Ask me any research question and I'll generate a detailed, well-structured report.",
    textbox=gr.Textbox(placeholder="Type your research question here...", container=True),
    theme="default",
    examples=["What are the impacts of AI on healthcare?"],
    
).launch()
