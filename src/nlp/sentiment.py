from transformers import pipeline

# Load model once (important for performance)
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def get_sentiment(text):
    result = sentiment_model(text, truncation=True)[0]

    print("result:", result)

    return {
        "label": result["label"],
        "score": result["score"]
    }