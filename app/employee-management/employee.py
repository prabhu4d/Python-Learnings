import csv
import sys


class Employee:
    total = 0

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        Employee.total += 1

    def __str__(self):
        return f"{self.name} was {self.age} old, working as {self.occupation}"


EmployeesObjects = []


def read_employees():
    with open('employees.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            EmployeesObjects.append(Employee(row[0], row[1], row[2]))
    return True


def show_employees():
    print(f"\nEmployees Strength : {Employee.total}")
    for i, emp in enumerate(EmployeesObjects):
        print(f"{i} : {emp}")
    print("\n")


def save_employees():
    with open('employees.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for emp in EmployeesObjects:
            writer.writerow([emp.name, emp.age, emp.occupation])
    return True


# Main
read_employees()

option = None


def check_valid():
    x = input(
        "You Entered Wrong Command, \nDo you want to continue or exit (y or n) ")
    if x == "":
        check_valid()
    elif x == "n":
        quit()
    elif x == "y":
        options()
    else:
        check_valid()


def options():
    print("1. Entering Employee Data")
    print("2. Show the Employees Details")
    print("3. Quit Application")
    global option
    x = input("Enter (1 or 2 or 3) : ")
    if x == "":
        check_valid()
    else:
        try:
            option = int(x)
        except ValueError as e:
            print(e)
            check_valid()


print("*"*60)
print("               OneData Software Solutions")
print("*"*60)
print(f"Employees Strength : {Employee.total}\n")

options()


def quit():
    save_employees()
    print("Done")
    sys.exit()


while True:
    if option == 1:
        current_employee = 1
        enter = True
        print("S.No Name Age Occupation")
        while enter:
            emp = input(f"{current_employee} : ")
            if emp == "":
                enter = False
                check_valid()
            else:
                details = emp.split(" ")
                EmployeesObjects.append(
                    Employee(details[0], details[1], details[2]))
                current_employee += 1
    elif option == 2:
        show_employees()
        options()
    elif option == 3:
        quit()
    else:
        check_valid()
