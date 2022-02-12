from person import Employee, Owner, Client
from team import Team
from project import Project

# Owner
raja = Owner("Raja", 40, "raja@gmail.com", 'usa', 'OneData')

# Teams
java = Team("Java")
python = Team("Python")
react = Team("React")
devops = Team("DevOps")


# Employees
prabhu = Employee("Prabhu", 23, 'prabhu@gmail.com', 'cbe')
prasanth = Employee("Prasanth", 24, 'prasanth@gmail.com', 'cbe')
kannan = Employee("Kannan", 30, 'kannan@gmail.com', 'cbe')
kumaran = Employee("Kumaran", 24, 'kumaran@gmail.com', 'cbe')
priyanka = Employee("Priyanka", 25, 'priyanka@gmail.com', 'cbe')
rabiya = Employee("Rabiya", 25, 'rabiya@gmail.com', 'cbe')
rampriya = Employee("Ram Priya", 25, 'rampriya@gmail.com', 'cbe')
jana = Employee("Jana", 30, 'jana@gmail.com', 'cbe')
kuppu = Employee("Kuppu", 30, 'kuppu@gmail.com', 'cbe')
gowtham = Employee("Gowtham", 25, 'gowtham@gmail.com', 'cbe')


# Adding Employees to Team
java.add_employee(kuppu)
java.add_employee(prasanth)

python.add_employee(kannan)
python.add_employee(prabhu)
python.add_employee(kumaran)
python.add_employee(priyanka)
python.add_employee(rabiya)

react.add_employee(jana)
react.add_employee(rampriya)

devops.add_employee(gowtham)

java.add_employee(kannan)

# Clients
suresh = Client('Suresh', 30, 'suresh@gmail.com', 'London', 'DataLake')
ramesh = Client('Ramesh', 28, 'ramesh@gmail.com', 'Dubai', 'KG')

#  Project
onecare = Project("OneCare", "Health Care Application", ramesh)
etl = Project("ETL", "Data Engieering Tools", suresh)

onecare.add_team(python)
onecare.add_team(java)

etl.add_team(python)
etl.add_team(devops)

# Employee.details()
# Team.details()
# Client.details()
# Project.details()