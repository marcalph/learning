from transformers import AutoModel, AutoModelForSequenceClassification, AutoTokenizer, pipeline


clf = pipeline("sentiment-analysis")
text_inputs = [
    "This is the way!",
    "I hate all of this so much I could die"
]


ckpt = "distilbert-base-uncased-finetuned-sst-2-english"
tok = AutoTokenizer.from_pretrained(ckpt)
# mdl = AutoModel.from_pretrained(ckpt)
mdl_clf = AutoModelForSequenceClassification.from_pretrained(ckpt)
# model_inputs = tok(text_inputs, padding=True, truncation=True, return_tensors="pt")

# model_ouputs = mdl(**model_inputs)
# model_clf_ouputs = mdl_clf(**model_inputs)

# tokenized = tok.tokenize(text_inputs)
# converted = tok.convert_tokens_to_ids(tokenized)
# prepared = tok.prepare_for_model(converted)
# decoded = tok.decode(prepared["input_ids"])

sequence = "I've been waiting for a HuggingFace course my whole life."

tokens = tok.tokenize(sequence)
ids = tok.convert_tokens_to_ids(tokens)
import torch
input_ids = torch.tensor([ids])
print("Input IDs:", input_ids)

output = mdl_clf(input_ids)
print("Logits:", output.logits)


if __name__ == "__main__":
    batched_ids = [ids, ids]
    batched_inputs = torch.tensor(batched_ids)
    outs = mdl_clf(batched_inputs)
    print(outs)
    # print(text_inputs)
    # print(tokenized)
    # print(converted)
    # print(prepared)
    # print(decoded)
    # print(clf(text_inputs))
    # print(model_inputs)
    # print(model_ouputs)
    # print("#####")
    # print(model_clf_ouputs)
