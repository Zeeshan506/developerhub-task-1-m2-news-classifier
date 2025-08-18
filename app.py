import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

st.title("📰 News Topic Classifier")

# Load locally trained model
model_path = "./models/news_classifier"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

label_map = {0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}

text = st.text_area("Enter a news headline:")

if st.button("Classify"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
        outputs = model(**inputs)
        preds = torch.argmax(outputs.logits, dim=1).item()
        st.success(f"Predicted Category: {label_map[preds]}")
