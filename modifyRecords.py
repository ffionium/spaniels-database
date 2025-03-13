import sqlite3
import os

DATABASE_FILE = "spaniels_data.db"

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS springer_spaniels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT NOT NULL,
            spots TEXT NOT NULL,  -- Store 'Yes' or 'No' instead of Boolean
            favourite_toy TEXT,
            favourite_treat TEXT
        )
    """)

    # save & close
    conn.commit()
    conn.close()   


def insert_record(springer):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    print(springer.name)

    cursor.execute("""
        INSERT INTO springer_spaniels (name, gender, spots, favourite_toy, favourite_treat)
        VALUES (?, ?, ?, ?, ?)
    """, (springer.name, springer.gender, springer.spots, springer.favourite_toy, springer.favourite_treat))

    conn.commit()
    conn.close()
    
    print("Records have been written to the database!")
    

def delete_record(identifier):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Check if identifier is a number (ID) or text (name)
    if identifier.isdigit():
        cursor.execute("SELECT * FROM springer_spaniels WHERE id = ?", (identifier,))
    else:
        cursor.execute("SELECT * FROM springer_spaniels WHERE name = ?", (identifier,))

    # retrieves rows
    record = cursor.fetchone()

    if not record:
        print("No matching record found.")
        conn.close()
        return

    print("Found record:")
    print(f"ID: {record[0]}, Name: {record[1]}, Gender: {record[2]}, Spots: {record[3]}, Toy: {record[4]}, Treat: {record[5]}")
    
    confirm = input("Are you sure you want to delete this record? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        conn.close()
        return

    if identifier.isdigit():
        cursor.execute("DELETE FROM springer_spaniels WHERE id = ?", (identifier,))
    else:
        cursor.execute("DELETE FROM springer_spaniels WHERE name = ?", (identifier,))

    conn.commit()
    conn.close()
    
    print("Record deleted successfully!")




