import pandas as pd
import psycopg2



def run_verification_queries(cursor):

    print("\n--- Verification Queries ---")

    # ----------------------------------------
    # Count reviews per bank
    # ----------------------------------------

    query_1 = """
    SELECT b.bank_name, COUNT(*) AS total_reviews
    FROM reviews r
    JOIN banks b
    ON r.bank_id = b.bank_id
    GROUP BY b.bank_name;
    """

    cursor.execute(query_1)

    print("\nTotal Reviews Per Bank:")

    for row in cursor.fetchall():
        print(row)

    # ----------------------------------------
    # Average rating per bank
    # ----------------------------------------

    query_2 = """
    SELECT b.bank_name, AVG(r.rating) AS avg_rating
    FROM reviews r
    JOIN banks b
    ON r.bank_id = b.bank_id
    GROUP BY b.bank_name;
    """

    cursor.execute(query_2)

    print("\nAverage Rating Per Bank:")

    for row in cursor.fetchall():
        print(row)

    # ----------------------------------------
    # Check missing values
    # ----------------------------------------

    query_3 = """
    SELECT COUNT(*)
    FROM reviews
    WHERE review_text IS NULL
       OR rating IS NULL;
    """

    cursor.execute(query_3)

    null_count = cursor.fetchone()[0]

    print("\nMissing Critical Values:")
    print(null_count)




# -------------------------------------------
# PostgreSQL connection
# -------------------------------------------

conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

print("Database connected successfully!")

df = pd.read_csv("data/raw/task2_output.csv")

banks = [
    ("CBE", "com.combanketh.mobilebanking"),
    ("BOA", "com.boa.boaMobileBanking"),
    ("Dashen", "com.dashen.dashensuperapp")
]

insert_bank_query = """
INSERT INTO banks (bank_name, app_name)
VALUES (%s, %s)
ON CONFLICT DO NOTHING;
"""

for bank in banks:
    cursor.execute(insert_bank_query, bank)

conn.commit()


cursor.execute("SELECT bank_id, bank_name FROM banks;")

bank_mapping = {
    name: bank_id
    for bank_id, name in cursor.fetchall()
}

print(bank_mapping)


insert_review_query = """
INSERT INTO reviews (
    bank_id,
    review_text,
    rating,
    review_date,
    sentiment_label,
    sentiment_score,
    identified_theme,
    source
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_review_query,
        (
            bank_mapping[row["bank"]],
            row["review"],
            int(row["rating"]),
            row["date"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["identified_theme"],
            row["source"]
        )
    )

conn.commit()

print("Reviews inserted successfully!")

run_verification_queries(cursor)

cursor.close()
conn.close()

print("Database connection closed.")


