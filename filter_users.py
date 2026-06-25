import json


def filter_users_by_name(name):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        filtered_users = [user for user in users if user["name"].lower() == name.lower()]

        for user in filtered_users:
            print(user)

    except FileNotFoundError:
        print("User not found.")


def filter_users_by_age(age):
    try:
            with open("users.json", "r") as file:
                users = json.load(file)

            filtered_users = [user for user in users if user["age"] == age]

            for user in filtered_users:
                print(user)
    except FileNotFoundError:
        print("User not found.")


def filter_users_by_email(email):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        filtered_users = [user for user in users if user["email"] == email]

        for user in filtered_users:
            print(user)
    except FileNotFoundError:
        print("User not found.")
