import modifyRecords
import os

def main():

    while True:
        print("Springer Spaniels Database Application")
        print("1. Add a new Springer Spaniel")
        print("2. View all records")
        print("3. Delete a record by name or id.")
        print("4. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter dog's name: ")
            sex = input("Enter dog's sex (Male/Female): ")
            spots = input("Does the dog have spots? (Yes/No): ")
            favourite_toy = input("Enter dog's favorite toy: ")
            favourite_treat = input("Enter dog's favorite treat: ")
            modifyRecords.insert_record(name, sex, spots, favourite_toy, favourite_treat)
            print("Record added successfully!")

        elif choice == "2":
            os.system("python c:\\Users\\Ffiz_\\Documents\\Coding\\Python\\spaniels-database\\viewDatabase.py")
            # viewDatabase.runGUI()
            # display_records()
            
        elif choice == "3":
            spanielToDel = input("Enter name or id of record to delete: ")
            modifyRecords.delete_record(spanielToDel)  

        elif choice == "4":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Run the application
if __name__ == "__main__":
    main()