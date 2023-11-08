
import json

# Empty dictionary to store username and password
user_data = {}

#Function to load user data from JSON file 
def load_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data.update(json.load(file))
        print("User data loaded.")
    except FileNotFoundError:
        print("User data not found.")

#Function to save user data in JSON file format
def save_data():
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    print("User data saved!")

#Function to register with new username and password
def register():
    username = input("\nEnter username: ")
    if username in user_data:
        print("Username already exists.")
    else:
        password = input("Enter password: ")
        user_data[username] = password
        save_data()
        print("Registration successful.")

#Function to login with registered username and password.
def login():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    if username in user_data and user_data[username] == password:
        print("\nLogin successful.")
    else:
        print("\nLogin failed.")

#Function to call the load user data
load_data()

#Main menu
while True:
    print("\nWelcome to the login page.")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        save_data()
        break
    else:
        print("\nEnter a valid option.")
