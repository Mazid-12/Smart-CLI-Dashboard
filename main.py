from User import *
import json

def print_menu():
    print("===== MENU =====")
    print("1. View profile \n2. See Weather \n3. Convert currency \n4. Search history \n0. Exit")


def create_file():
    user_list = []
    with open("user.json", "w") as file:
        json.dump(user_list, file, indent=4)
create_file()








