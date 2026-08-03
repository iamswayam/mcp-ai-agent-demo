import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "ezauto.db"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def run_query(title, query):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    cursor.execute(query)

    rows = cursor.fetchall()

    if not rows:
        print("No results")
        return

    for row in rows:
        print(dict(row))


# --------------------------
# Total Cases
# --------------------------
run_query(
    "Total Cases",
    """
    SELECT COUNT(*) AS total_cases
    FROM cases;
    """
)

# --------------------------
# Cases By Status
# --------------------------
run_query(
    "Cases By Status",
    """
    SELECT status,
           COUNT(*) AS total
    FROM cases
    GROUP BY status;
    """
)

# --------------------------
# Top Rated Vendors
# --------------------------
run_query(
    "Top Rated Vendors",
    """
    SELECT name,
           city,
           rating
    FROM vendors
    ORDER BY rating DESC
    LIMIT 5;
    """
)

# --------------------------
# Cases Per Brand
# --------------------------
run_query(
    "Cases Per Brand",
    """
    SELECT
        b.name,
        COUNT(*) AS total_cases
    FROM cases c
    JOIN client_brands b
      ON c.vehicle_brand_id = b.id
    GROUP BY b.name
    ORDER BY total_cases DESC;
    """
)

conn.close()