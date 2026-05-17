## Data Collection Methodology

### Overview
This project collects user reviews from the Google Play Store for three Ethiopian banking applications:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to transform unstructured user feedback into structured data for sentiment analysis and thematic exploration.

---

### Data Source
All data was collected from the Google Play Store using the `google-play-scraper` Python library.

---

### Scraping Approach

A Python-based automated scraping pipeline was developed to extract reviews for each banking app using their Google Play package IDs.

For each app, the following steps were performed:

1. Query the Google Play Store using the app’s package name.
2. Extract user reviews including:
   - Review text
   - Star rating (1–5)
   - Review timestamp
3. Repeat the process for all three bank applications.
4. Combine all reviews into a single structured dataset.

---

### Data Fields Collected
Each review record contains the following attributes:

- `review`: User feedback text
- `rating`: Star rating (1 to 5)
- `date`: Review date in YYYY-MM-DD format
- `bank`: Name of the bank application
- `source`: Data source (Google Play Store)

---

### Data Volume
- Minimum target: 400 reviews per bank
- Total target: 1,200+ reviews

If scraping limitations occur (e.g., API rate limits or missing data), the issue is documented and a broader time range is used to increase coverage.

---

### Data Storage
- Raw data is stored locally under: `data/raw/`
- Cleaned datasets are generated after preprocessing and used for analysis

---

### Limitations
- Google Play Store may restrict the number of retrievable reviews per request
- Some older reviews may not be accessible depending on API response limits
- Review text quality varies (short comments, emojis, or missing context)

---

### Tools Used
- Python
- google-play-scraper
- pandas