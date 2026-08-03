-- Remove old tables if they exist
DROP TABLE IF EXISTS cases;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS client_brands;


-- ==========================
-- Client Brands
-- ==========================
CREATE TABLE client_brands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    vehicle_type TEXT NOT NULL
);


-- ==========================
-- Vendors
-- ==========================
CREATE TABLE vendors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    vendor_type TEXT NOT NULL,
    city TEXT NOT NULL,
    rating REAL NOT NULL,
    available BOOLEAN NOT NULL
);


-- ==========================
-- Cases
-- ==========================
CREATE TABLE cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,

    vehicle_brand_id INTEGER NOT NULL,
    vendor_id INTEGER,

    city TEXT NOT NULL,

    status TEXT NOT NULL,

    created_at TEXT NOT NULL,

    FOREIGN KEY(vehicle_brand_id)
        REFERENCES client_brands(id),

    FOREIGN KEY(vendor_id)
        REFERENCES vendors(id)
);