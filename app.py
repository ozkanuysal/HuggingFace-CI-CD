from transformers import pipeline
import gradio as gr 


model = pipeline('summarization')

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbook = gr.Textbox(placeholder="Enter a text for summary.",lines=4)
    gr.Interface(fn=predict, inputs=textbook, outputs="text")

demo.launch()