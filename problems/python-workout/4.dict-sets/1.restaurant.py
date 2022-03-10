MENU = {"tea": 10, "vada": 6, "coffee": 15, "ponda": 8, "puffs": 12}


def restaurant():
    total = 0
    while True:
        order = input("Order: ").strip()

        if not order:
            break

        try:
            price = MENU[order]
            total += price
            print(f"{order} is {price}, total is {total}")
        except:
            print(f"Sorry, we are fresh out of {order} today")

    print(f"Your total is {total}")


restaurant()


# Beyond the Exercises

"""
Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry. (Note: This is a nice
little exercise, but please never store unencrypted passwords. It’s a major secu-
rity risk.)
"""

USERS = {"prabhu": "1234", "vignesh": "2345", "john": "4567"}


def user_management():
    username = input("Enter your username: ").strip()

    try:
        password = USERS[username]
        password_entered = input("Enter the Password: ").strip()
        if password == password_entered:
            print("Login Successfull")
        else:
            print("Password Invalid")
    except KeyError as e:
        print(f"Invalid username {username}")


user_management()


"""
Define a dict whose keys are dates (represented by strings) from the most recent
week and whose values are temperatures. Ask the user to enter a date, and dis-
play the temperature on that date, as well as the previous and subsequent dates,
if available.
"""

"""
Define a dict whose keys are names of people in your family, and whose values
are their birth dates, as represented by Python date objects (http://mng.bz/
jggr). Ask the user to enter the name of someone in your family, and have the
program calculate how many days old that person is.
"""
