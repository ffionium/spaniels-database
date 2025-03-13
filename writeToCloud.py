from google.cloud import firestore
import sqlite3

DATABASE_FILE = "spaniels_data.db"

def push_to_cloud():
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    # set connection w/ key 
    credsPath = "c:\\Users\\Ffiz_\\Documents\\Coding\\Python\\spaniels-database\\Gcloud_key"
    db = firestore.Client.from_service_account_json(credsPath)
    
    cursor.execute("SELECT id, name, gender, spots, favourite_toy, favourite_treat FROM springer_spaniels") 
    records = cursor.fetchall()

    # Upload to Firestore
    for record in records:
        id, name, gender, spots, favourite_toy, favourite_treat = record  
        db.collection("springer_spaniels").document(str(id)).set({
            "id": id,
            "name": name,
            "gender": gender,
            "spots": spots,
            "favourite_toy": favourite_toy,
            "favourite_treat": favourite_treat            
        })

    # batch = db.batch()
    # for record in records:
    #     doc_id, name, age, email = record
    #     doc_ref = db.collection("users").document(str(doc_id))
    #     batch.set(doc_ref, {"name": name, "age": age, "email": email})
    # batch.commit()

    # Close database connection
    conn.close()
    print("Data successfully uploaded to Firestore!")