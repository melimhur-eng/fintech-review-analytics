# Raw data might contain many nices like emojis, casing issues, punctuations and so on
# so we need to clean it first
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)  # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars
    text = re.sub(r"\s+", " ", text).strip()
    return text