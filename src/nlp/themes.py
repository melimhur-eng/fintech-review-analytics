from sklearn.feature_extraction.text import TfidfVectorizer
THEME_RULES = {
    "login": "Account Access Issues",
    "otp": "Account Access Issues",
    "password": "Account Access Issues",

    "slow": "Performance Issues",
    "loading": "Performance Issues",
    "transfer": "Transaction Performance",

    "ui": "UI & Design",
    "interface": "UI & Design",

    "error": "App Stability Issues",
    "crash": "App Stability Issues"
}

def extract_keywords(corpus, max_features=50):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=max_features)
    X = vectorizer.fit_transform(corpus)

    return vectorizer.get_feature_names_out()

def assign_theme(text):
    for keyword, theme in THEME_RULES.items():
        if keyword in text:
            return theme
    return "Other"