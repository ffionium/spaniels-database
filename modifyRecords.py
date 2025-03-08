import sqlite3

# Database file name
DATABASE_FILE = "spaniels_data.db"

# Function to create the table (if it doesn't exist)
def create_table():
    conn = sqlite3.connect(DATABASE_FILE)  # Connect to SQLite database file
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

    conn.commit()  # Save changes
    conn.close()   # Close connection

# Function to insert a record into the database
def insert_record(name, gender, spots, favourite_toy, favourite_treat):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO springer_spaniels (name, gender, spots, favourite_toy, favourite_treat)
        VALUES (?, ?, ?, ?, ?)
    """, (name, gender, spots, favourite_toy, favourite_treat))

    conn.commit()
    conn.close()
    
    print("Records have been written to the database!")


# Function to delete a record by ID or name
def delete_record(identifier):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Check if identifier is a number (ID) or text (name)
    if identifier.isdigit():
        cursor.execute("SELECT * FROM springer_spaniels WHERE id = ?", (identifier,))
    else:
        cursor.execute("SELECT * FROM springer_spaniels WHERE name = ?", (identifier,))

    # retrieves row of query result
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

    # Perform the deletion
    if identifier.isdigit():
        cursor.execute("DELETE FROM springer_spaniels WHERE id = ?", (identifier,))
    else:
        cursor.execute("DELETE FROM springer_spaniels WHERE name = ?", (identifier,))

    conn.commit()
    conn.close()
    
    print("Record deleted successfully!")




