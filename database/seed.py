import sqlite3
from pathlib import Path

import random
from faker import Faker

fake = Faker("en_IN")


# Project paths
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "ezauto.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"

# Create database connection
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Execute schema.sql
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

print("Database schema created successfully.")


# -----------------------------
# Insert Client Brands
# -----------------------------

brands = [
    ("Royal Enfield", "2 Wheeler"),
    ("Honda", "2 Wheeler"),
    ("TVS", "2 Wheeler"),
    ("Bajaj", "2 Wheeler"),
    ("Hero", "2 Wheeler"),
    ("Hyundai", "4 Wheeler"),
    ("Maruti Suzuki", "4 Wheeler"),
    ("Mahindra", "4 Wheeler"),
    ("Tata Motors", "4 Wheeler"),
    ("Kia", "4 Wheeler"),
]

cursor.executemany(
    """
    INSERT INTO client_brands (name, vehicle_type)
    VALUES (?, ?)
    """,
    brands,
)

conn.commit()

print(f"Inserted {len(brands)} client brands.")


# -----------------------------
# Insert Vendors
# -----------------------------

cities = [
    "Bengaluru",
    "Hyderabad",
    "Delhi",
    "Mumbai",
    "Chennai",
    "Pune",
]

vendor_types = [
    "RE_AUTHORIZED",
    "THIRD_PARTY",
]

vendors = []

for i in range(50):
    vendors.append(
        (
            f"{random.choice(['RoadAssist','QuickTow','AutoCare','CityRescue'])} {random.choice(cities)}",
            random.choice(vendor_types),
            random.choice(cities),
            round(random.uniform(3.5, 5.0), 1),
            random.choice([0, 1]),
        )
    )

cursor.executemany(
    """
    INSERT INTO vendors
    (name, vendor_type, city, rating, available)
    VALUES (?, ?, ?, ?, ?)
    """,
    vendors,
)

conn.commit()

print(f"Inserted {len(vendors)} vendors.")


# -----------------------------
# Insert Cases
# -----------------------------

statuses = [
    "CREATED",
    "PENDING_ASSIGNMENT",
    "ASSIGNED",
    "ESCALATED",
    "RESOLVED",
    "CLOSED",
]

cases = []

for _ in range(300):

    customer_name = fake.name()

    vehicle_brand_id = random.randint(1, 10)

    vendor_id = random.choice(
        [None] + list(range(1, 51))
    )

    city = random.choice(cities)

    status = random.choice(statuses)

    created_at = fake.date_time_this_year().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cases.append(
        (
            customer_name,
            vehicle_brand_id,
            vendor_id,
            city,
            status,
            created_at,
        )
    )

cursor.executemany(
    """
    INSERT INTO cases
    (
        customer_name,
        vehicle_brand_id,
        vendor_id,
        city,
        status,
        created_at
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    cases,
)

conn.commit()

print(f"Inserted {len(cases)} cases.")


conn.close()

print("\nDatabase ready!")