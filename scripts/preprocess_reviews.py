import pandas as pd


df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial shape:", df.shape)


df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

df = df.dropna(subset=['review', 'rating'])

print("After removing missing values:", df.shape)

df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')


df = df[df['review'].str.strip() != ""]


df.to_csv("data/raw/clean_reviews.csv", index=False)

print("Cleaned dataset saved successfully!")
print(df.head())