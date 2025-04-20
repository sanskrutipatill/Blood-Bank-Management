import sqlite3

db = sqlite3.connect("bloodbankkk_manager.db")
cursor = db.cursor()

def db_query(query, params=None):
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    db.commit()
    return cursor.fetchall()

def create_tables():
    # Drop old tables to rebuild new structure
    cursor.execute("DROP TABLE IF EXISTS donor")
    cursor.execute("DROP TABLE IF EXISTS request")
    
    # Create the donor table with updated columns
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donor (
        donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_name TEXT,
        donor_age INTEGER,
        donor_gender TEXT,
        donor_blood_type TEXT,
        donor_weight REAL,
        donor_disease TEXT
    )
    """)

    # Create the request table with updated columns
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS request (
        request_id INTEGER PRIMARY KEY AUTOINCREMENT,
        hospital_name TEXT,
        patient_name TEXT,
        patient_age INTEGER,
        patient_gender TEXT,
        patient_blood_type TEXT,
        patient_weight REAL,
        patient_disease TEXT,
        donor_name TEXT,
        donor_age INTEGER,
        donor_gender TEXT,
        donor_blood_type TEXT
    )
    """)

    # Create the inventory table with blood types
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        blood_id INTEGER PRIMARY KEY AUTOINCREMENT,
        blood_type TEXT UNIQUE,
        quantity INTEGER
    )
    """)

    # Initialize inventory with unique blood types
    blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    for btype in blood_types:
        cursor.execute("SELECT * FROM inventory WHERE blood_type = ?", (btype,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO inventory (blood_type, quantity) VALUES (?, ?)", (btype, 0))

    db.commit()

create_tables()
