# 📰 News Topic Classifier

This project is a **news headline classification model** fine-tuned and deployed as a web application. It can categorize news headlines into one of four topics: World, Sports, Business, and Sci/Tech.

The project demonstrates a complete machine learning workflow, from training a model to deploying it for public use. 

***

## 🧠 What We Did

### 1. Model Training
We **fine-tuned a pre-trained `bert-base-uncased` model** on the AG News dataset. This process involved:
* Using the `transformers` library to handle tokenization and model training.
* Employing the `Trainer` API for efficient training.
* Using the `evaluate` library to track key metrics like **accuracy** and **F1 score** to ensure the model's performance.
* Configuring the training process to save the best model and **push it to the Hugging Face Hub** for public use.

### 2. Model Deployment
We **deployed the trained model** as a live, interactive web demo using Gradio. This was done by:
* Loading the fine-tuned model directly from the Hugging Face Hub.
* Writing a simple function that takes a news headline as input and returns the predicted category.
* Using `gr.Interface` to create a user-friendly web interface with a text box for input and a label for output.
* Explicitly mapping the model's integer labels (e.g., `0`, `1`) to human-readable names (`World`, `Sports`, etc.) to ensure the app displays clear results.
* Launching the Gradio app to generate a **shareable public link**.

## 🚀 How to Use the App

You can access the live demo on Hugging Face Spaces. Simply enter a news headline and click "Classify". The app will provide the predicted category and its confidence score.

* [ Deployment](https://12455162c1d8801075.gradio.live/)

**Example headlines:**
* `Apple unveils new AI-powered iPhone with improved camera`
* `Local team wins championship with last-second shot`
* `Stock market soars as inflation fears ease`

***

## 🔗 Model and Libraries

* **Model:** [`Zeeshan506/news-classifier`](https://huggingface.co/Zeeshan506/news-classifier)
* **Libraries:** `transformers`, `torch`, `gradio`, `evaluate`, `datasets`

***

## 🤝 Acknowledgements

* **Hugging Face**: For providing powerful libraries and a platform for model hosting.
* **Gradio**: For the simple and effective tool for building and sharing ML demos.
* **AG News Dataset**: For the data used to train the model.
