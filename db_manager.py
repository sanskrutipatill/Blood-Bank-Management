import mysql.connector
from db_config import DB_CONFIG
import sys

# Global connection and cursor
db = None
cursor = None

def get_db_connection():
    global db, cursor
    try:
        if db is None or not db.is_connected():
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()
            print("Connected to MySQL database")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # Fallback or exit? For now, let's print and maybe exit if critical
        if err.errno == 1049: # Unknown database
            print(f"Database '{DB_CONFIG['database']}' does not exist. Please create it or check config.")
        return None
    return db

def db_query(query, params=None):
    global db, cursor
    try:
        get_db_connection()
        if db is None:
            return []
            
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE", "CREATE", "DROP")):
            db.commit()
            return cursor.fetchall() # Usually empty for these, but consistent with original
        else:
            return cursor.fetchall()
            
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []

def init_db():
    """Initializes the database tables if they don't exist."""
    print("Initializing Database...")
    create_conn = None
    try:
        # Connect to server directly to create DB if needed
        temp_config = DB_CONFIG.copy()
        db_name = temp_config.pop('database')
        create_conn = mysql.connector.connect(**temp_config)
        c = create_conn.cursor()
        c.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        create_conn.commit()
        c.close()
        create_conn.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

    # Now create tables
    get_db_connection()
    
    # Create donor table
    db_query("""
    CREATE TABLE IF NOT EXISTS donor (
        donor_id INT AUTO_INCREMENT PRIMARY KEY,
        donor_name VARCHAR(255),
        donor_age INT,
        donor_gender VARCHAR(50),
        donor_blood_type VARCHAR(10),
        donor_weight FLOAT,
        donor_disease VARCHAR(255)
    )
    """)

    # Create request table
    db_query("""
    CREATE TABLE IF NOT EXISTS request (
        request_id INT AUTO_INCREMENT PRIMARY KEY,
        hospital_name VARCHAR(255),
        patient_name VARCHAR(255),
        patient_age INT,
        patient_gender VARCHAR(50),
        patient_blood_type VARCHAR(10),
        patient_weight FLOAT,
        patient_disease VARCHAR(255),
        donor_name VARCHAR(255),
        donor_age INT,
        donor_gender VARCHAR(50),
        donor_blood_type VARCHAR(10)
    )
    """)

    # Create inventory table
    db_query("""
    CREATE TABLE IF NOT EXISTS inventory (
        blood_id INT AUTO_INCREMENT PRIMARY KEY,
        blood_type VARCHAR(10) UNIQUE,
        quantity INT
    )
    """)

    # Initialize inventory
    blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    for btype in blood_types:
        res = db_query("SELECT * FROM inventory WHERE blood_type = %s", (btype,))
        if not res:
            db_query("INSERT INTO inventory (blood_type, quantity) VALUES (%s, %s)", (btype, 0))
    
    print("Database Initialized.")

if __name__ == "__main__":
    init_db()
