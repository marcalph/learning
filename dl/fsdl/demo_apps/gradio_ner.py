from transformers import pipeline
import gradio as gr

ner_pipeline = pipeline('ner', aggregation_strategy="simple")

examples = ["Queen Lizzie died this month",
            "My name is JD and I live in Chicago",]

def ner(text):
    output = ner_pipeline(text)
    for ent in output:
        ent["entity"] = ent.pop("entity_group")
    return {"text": text, "entities": output}

demo = gr.Interface(ner,
             gr.Textbox(placeholder="Enter sentence here..."),
             gr.HighlightedText(),
             examples=examples)

demo.launch()