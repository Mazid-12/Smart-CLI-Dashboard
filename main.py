from User import *
import json
from datetime import datetime

def print_menu():
    print("\n===== MENU =====")
    print("1. View profile \n2. See Weather \n3. Convert currency \n4. Search history \n0. Exit")

def create_file():
    user_list = []
    with open("user.json", "w") as file:
        json.dump(user_list, file, indent=4)

def sign_up(name):
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

def login(user_name):
    with open("user.json", 'r') as file:
        user_data = json.load(file)
    for user_dict in user_data:
        if user_dict['name'] == user_name:

            current_user = User.create_user(user_dict['name'], user_dict['creation_date'])
            return current_user 
    else:
            return False

def main():
    while True:
        username = input("Enter you name: ")
        user = login(username)
        if user == False:
            print("You don't have an account. Please, sign up!")
            singup_name = input("We're signin you up. Please enter your name: ")
            sign_up(singup_name)
            print("Now, you have to sign in!")
            continue
        else:
            print("You're logged in!")
            break

    while True:
        try:  
            print_menu()
            user_choice = int(input('Enter your choice: '))
            match user_choice:
                case 1:
                    print(user.view_profile())   
                case 2:
                    print(user.get_weather())      
                case 3:
                    print(user.convert_currency())       
                case 4:
                    print("not yet available!")
                case _:
                    break 
                    
        except ValueError:
            print("Invalid Input")     


main()

            