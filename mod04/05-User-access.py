username = "python"
password = "rules"
tries = 5

while tries > 0:
    un_input = input("Enter your username: ")
    pw_input = input("Enter your password: ")

    if un_input == username and pw_input == password:
        print("Welcome!")
        break
    else:
        tries -= 1
        if tries > 0:
            print("\nYour username or password is wrong. Please try again.")
        else:
            print("Access denied!")