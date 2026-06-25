import json


def filter_users_by_name(name):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        filtered_users = [user for user in users if user["name"].lower() == name.lower()]

        if len(filtered_users) == 0:
            print("No users found with that name.")
        else:
            for user in filtered_users:
                print(user)

    except FileNotFoundError:
        print("User not found.")


def filter_users_by_age(age):
    try:
            with open("users.json", "r") as file:
                users = json.load(file)

            filtered_users = [user for user in users if user["age"] == age]

            if len(filtered_users) == 0:
                print("No users found with that age.")
            else:
                for user in filtered_users:
                    print(user)

    except FileNotFoundError:
        print("User not found.")


def filter_users_by_email(email):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        filtered_users = [user for user in users if user["email"] == email]

        if len(filtered_users) == 0:
            print("No users found with that email.")
        else:
            for user in filtered_users:
                print(user)

    except FileNotFoundError:
        print("User not found.")
