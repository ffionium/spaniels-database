import tkinter as tk
from tkinter import ttk
import sqlite3

# Function to fetch data from database
def fetch_data():
    conn = sqlite3.connect("spaniels_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM springer_spaniels")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Create GUI window
root = tk.Tk()
root.title("Springer Spaniels Database Viewer")
root.geometry("1200x400")

# Create Treeview (Table)
tree = ttk.Treeview(root, columns=("ID", "Name", "Gender", "Spots", "Favourite Toy", "Favourite Treat"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Gender", text="Gender")
tree.heading("Spots", text="Spots")
tree.heading("Favourite Toy", text="Favourite Toy")
tree.heading("Favourite Treat", text="Favourite Treat")

# Insert data into Treeview
for row in fetch_data():
    tree.insert("", tk.END, values=row)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Pack widgets
tree.pack(expand=True, fill="both", padx=8, pady=8)
scrollbar.pack(side="right", fill="y")

# Run the GUI
root.mainloop()
    

