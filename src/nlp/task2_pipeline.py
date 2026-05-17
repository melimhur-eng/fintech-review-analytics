import pandas as pd
from preprocess import clean_text
from sentiment import get_sentiment
from themes import assign_theme

# Load data
df = pd.read_csv("data/raw/clean_reviews.csv")



# Clean text
df["clean_text"] = df["review"].apply(clean_text)

# Sentiment analysis
sentiments = df["clean_text"].apply(get_sentiment)

df["sentiment_label"] = sentiments.apply(lambda x: x["label"])
df["sentiment_score"] = sentiments.apply(lambda x: x["score"])

# Theme assignment
df["identified_theme"] = df["clean_text"].apply(assign_theme)

# Save result
df.to_csv("data/raw/task2_output.csv", index=False)

print("Task 2 pipeline completed!")
print(df.head())