
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name,age,occu):
        super().__init__(name, age)
        self.occu=occu
        self.__salary = 10000

    def eating(self):
        return f"{self.name} eating:"

    def sleep(self):
        return "employee sleeping:"

    def working(self):
        return f"{self.name} is working as {self.occu}"

    def showSalary(self):
        return self.__salary

    def setSalary(self, personType, salary):
        if personType == "HR":
            self.__salary = salary
            return "Successful"
        else:
            return "You Can't Assign Salary"

    def __str__(self):
        return f"{self.name} is {self.age} old and working as {self.occu}"

class Student(Person):
    def __init__(self,name,age,learning_sub):
        super().__init__(name, age)
        self.learning_sub=learning_sub

    def learning(self):
        return "student Learning subject:"

    def practicing(self):
        return "student practicing test:"

    def __str__(self):
        return f"{self.name} is {self.age} old and studying  {self.learning_sub}"


class Guru(Person):
    def __init__(self,name,age,experience,specialist):
        super.__init__(name, age)
        self.experience=experience
        self.specialist=specialist

    def teaching(self):
        return "Guru teaching subject:"

    def testing_student(self):
        return "Guru testing student:"

## Employee Creation
employees_data = [["rafs", 20, 'DS'], ['priya',25,'ML'], ['prabhu',25,'ML'], ['dhibakar',25,'ML'], ['srimaan',25,'ML']]

employeesObj = []

for employee in employees_data:
    employeesObj.append(Employee(employee[0], employee[1], employee[2]))

## Print all employee name
# for employee in employeesObj:
#     print(employee)




# Emp1=Employee('rafs',45,'DS')
# Emp2=Employee('priya',25,'ML')
# Emp3=Employee('prabhu',25,'ML')
# Emp4=Employee('dhibakar',25,'ML')
# Emp5=Employee('srimaan',25,'ML')

# print(Emp1.eating())
# print(Emp2.eating())
# print(Emp3.eating())
# print(Emp4.eating())
# print(Emp5.eating())

# print(Emp1.showSalary())
# print(Emp1.setSalary("HR", 20000))
# print(Emp1.showSalary())



# Stu1=Student('prabhu',22,'DA')
# Stu2=Student('prabhu',22,'DA')
# Stu3=Student('prabhu',22,'DA')
# Stu4=Student('prabhu',22,'DA')
# Stu5=Student('prabhu',22,'DA')

Student_data = [["rafs", 4, 'DS'], ['priya',25,'ML'], ['prabhu',25,'ML'], ['dhibakar',25,'ML'], ['srimaan',25,'ML']]

studentObj = []

for student in Student_data:
    studentObj.append(Student(student[0], student[1], student[2]))

print("\n Students ")
## Print all employee name
# for student in studentObj:
#     print(student)






# Guru1=Guru('kannan',25,12,'DA')
# Guru2=Guru('kannan',25,4,'DA')
# Guru3=Guru('kannan',25,7,'DA')
# Guru4=Guru('kannan',25,5,'DA')
# Guru5=Guru('kannan',25,6,'DA')

# print(Emp1.name,Emp1.age,Emp1.occu)
# print(Stu1.name,Stu1.age,Stu1.learning_sub)
# print(Guru1.name,Guru1.age,Guru1.experience,Guru1.specialist)

# Emp1.emp_eat()
# Emp2.emp_slee()
# Emp3.emp_work()

# Stu1.stu_learn()
# Stu2.stu_practice()

# Guru1.Guru_teaching()
# Guru2.Guru_testing_student()



prabhu = Employee("Prabhu", 22, "DS")
print(prabhu)
print(prabhu.working())