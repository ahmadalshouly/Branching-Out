from filter_users import filter_users_by_name, filter_users_by_email,filter_users_by_age

def main():
    valid_options = {"name": filter_users_by_name,
                     "age": filter_users_by_age,
                     "email": filter_users_by_email,}
    while True:
        try:
            filter_option = input("Enter your filter option (available options: name, age, email) or exit to close: ")

            if filter_option == "exit":
                break

            if filter_option not in valid_options:
                print("Please try again from the available options (name, age, email) or exit to close.")
                continue

            if filter_option == "age":
                while True:
                    age = input("Please enter the age you want to filter by: ")
                    if age.isdigit():
                        valid_options[filter_option](age)
                        break
                    print("Age must be a number. Please try again.")

            elif filter_option == "email":
                while True:
                    email = input("Please enter the email you want to filter by: ")
                    if "@"  in email and "."  in email:
                        valid_options[filter_option](email)
                        break
                    print("Email must contain @ and a dot. Please try again.")
            else:
                while True:
                    name = input("Please enter the name of the user you want to filter by: ")
                    if name.isalpha():
                        valid_options[filter_option](name)
                        break
                    print("Name must be a string. Please try again.")

        except ValueError:
            print("Invalid option. Please try again.")
            continue
        except Exception as err:
            print(f"Something went wrong. {err}")
            continue

if __name__ == "__main__":
    main()
