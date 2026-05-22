from User import *
import json
from datetime import datetime

def print_menu():
    print("===== MENU =====")
    print("1. View profile \n2. See Weather \n3. Convert currency \n4. Search history \n0. Exit")

def create_file():
    user_list = []
    with open("user.json", "w") as file:
        json.dump(user_list, file, indent=4)

def sign_up():
    name = input("Enter your name: ")
    long_date = datetime.now()
    date_creation = long_date.strftime("%Y-%m-%d")
    user = User.create_user(name, date_creation)
    user_dictionary = {'name' : name,
                       'creation_date' : date_creation}
    with open("user.json", 'r') as file:
        user_data = json.load(file)
        
    user_data.append(user_dictionary)

    with open("user.json", "w") as file:
        json.dump(user_data, file, indent=4)
    print("Your account has been successfully created!")

def login():
    user_name = input("Enter your name: ")
    with open("user.json", 'r') as file:
        user_data = json.load(file)
    for user_dict in user_data:
        if user_dict['name'] == user_name:
            current_user = User.create_user(user_dict['name'], user_dict['creation_date'])
            return current_user
        else:
            print("Your account hasn't been found!")

