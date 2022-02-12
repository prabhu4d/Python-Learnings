## Employee Variables
Employee1_name = "Pratheepa"
Employee1_age = 26
Employee1_occupation = "HR"

Employee2_name = "Ram priya"
Employee2_age = 24
Employee2_occupation = "Frontend Developer"

Employee3_name = "priya"
Employee3_age = 25
Employee3_occupation = "VP"

Employee4_name = "kowtham"
Employee4_age = 26
Employee4_occupation = "backend"

Employee5_name = "Pretheepa"
Employee5_age = 26
Employee5_occupation = "HR"



## Employee Functions
def eating(name):
    return f"{name} is Eating"

def sleeping():
    return "Employee is Sleeping"

def working():
    return "Employee is Working"

## Student Variables


Student1_name = "prabhu"
Student1_age = 21
Student1_learning_subject = "Data Science"


Student2_name = "priya"
Student2_age = 22
Student2_learning_subject = "Flask"

Student3_name = "rabiya"
Student3_age = 23
Student3_learning_subject = "Python"

Student4_name = "abi"
Student4_age = 23
Student4_learning_subject = "Data Anyltics"

Student5_name = "Kumaran"
Student5_age = 22
Student5_learning_subject = "ML"





## Student Functions
def learning():
    return "Student is learning"

def practicing():
    return "Student is practicing"

#Guru variable
Guru1_name = "Kannan"
Guru1_age = 22
Guru1_experience = "10"
Guru1_specialist="Full stack"

Guru2_name = "Kuppu"
Guru2_age= 28
Guru2_experience = "15"
Guru2_specialist="Full stack"

Guru3_name2 = "Gowtham"
Guru3_age2 = 28
Guru3_experience = 7
Guru3_specialist="AWS"

Guru4_name = "shudarsan"
Guru4_age = 25
Guru4_experience = 4
Guru4_specialist="Machine Learning"

Guru5_name = "mohanraj"
Guru5_age= 21
Guru5_experience = 12
Guru5_specialist="Data Science"


## Guru  Functions
def teaching():
    return "Guru is teaching"

def testing_student():
    return "Guru is testing student"






## Print all variables & Functions for Employee, Student, Guru
print(f"Employee 1 : {Employee1_name}, {Employee1_age}, and {Employee1_occupation}")
print(f"Employee 2 : {Employee2_name}, {Employee2_age}, and {Employee2_occupation}")
print(f"Employee 3 : {Employee3_name}, {Employee3_age}, and {Employee3_occupation}")
print(f"Employee 4: {Employee4_name}, {Employee4_age}, and {Employee4_occupation}")
print(f"Employee 5 : {Employee5_name}, {Employee5_age}, and {Employee5_occupation}")

print(eating(Employee1_name))
print(eating(Employee2_name))
print(eating(Employee3_name))
print(eating(Employee4_name))
print(eating(Employee5_name))

print(sleeping())
print(working())

#Student
print(f"Student 1 : {Student1_name}, {Student1_age}, and {Student1_learning_subject}")
print(f"Student 2 : {Student2_name}, {Student2_age}, and {Student2_learning_subject}")
print(f"Student 3 : {Student3_name}, {Student3_age}, and {Student3_learning_subject}")
print(f"Student 4 : {Student4_name}, {Student4_age}, and {Student4_learning_subject}")
print(f"Student 5 : {Student5_name}, {Student5_age}, and {Student5_learning_subject}")


print(learning())
print(practicing())


#Guru
print(f"Guru1 : {Guru1_name}, {Student1_age}, and {Student1_learning_subject}")
print(f"Guru 2 : {Student2_name}, {Student2_age}, and {Student2_learning_subject}")
print(f"Guru 3 : {Student3_name}, {Student3_age}, and {Student3_learning_subject}")
print(f"Guru 4 : {Student4_name}, {Student4_age}, and {Student4_learning_subject}")
print(f"Guru 5 : {Student5_name}, {Student5_age}, and {Student5_learning_subject}")


## Disadvantages of POP
"""
1. How to code large number of lines
2. Variables Accident
3. manually manage of the functions and variables
4. In POP everything is in open space, so anyone can access it
5. can't protect variables
"""
print("--- DisAdvantages ---")
print(Employee1_name)
Employee1_name = "Prabhu"
print(Employee1_name)

print(eating(Employee1_name))
print(teaching())