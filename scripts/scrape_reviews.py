from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime



apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}



all_reviews = []



for bank_name, package_name in apps.items():

    print(f"Scraping reviews for {bank_name}...")



    result, continuation_token = reviews(
        package_name,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )



    for review in result:

        all_reviews.append({
            "review": review['content'],
            "rating": review['score'],
            "date": review['at'].strftime('%Y-%m-%d'),
            "bank": bank_name,
            "source": "Google Play"
        })



df = pd.DataFrame(all_reviews)



df.to_csv("data/raw/bank_reviews_raw.csv", index=False)

print("Scraping completed successfully!")
print(df.head())