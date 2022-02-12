"""

"""


class DB:
    persons = []


class Person:
    def __init__(self, name, person_type):
        self.name = name
        self.type = person_type

    @classmethod
    def add(cls, name, person_type):
        DB.persons.append(cls(name, person_type))
        return DB.persons[-1]

    @classmethod
    def get_person(cls):
        persons = []
        for person in DB.persons:
            persons.append(person.name)
        return persons


class Employee(Person):
    def __init__(self, name):
        super().__init__(name, "Employee")

    @classmethod
    def add(cls, name):
        DB.persons.append(cls(name))
        return DB.persons[-1]

    @staticmethod
    def get_employee():
        employees = []
        for person in DB.persons:
            if person.type == "Employee":
                employees.append(person.name)
        return employees


class Student(Person):
    def __init__(self, name):
        super().__init__(name, "Student")

    @classmethod
    def add(cls, name):
        DB.persons.append(cls(name))
        return DB.persons[-1]

    @staticmethod
    def get_student():
        students = []
        for person in DB.persons:
            if person.type == "Student":
                students.append(person.name)
        return students


Person.add("Kannan", "Employee")
Person.add("Prabhu", "Student")

Employee.add("Jana")
Employee.add("Kuppu")
Employee.add("Ram Priya")
Employee.add("Kumaran")

Student.add("Rabiya")
Student.add("Priyanka")
Student.add("Dhibakar")
Student.add("Srimaan")

print("\nPersons --------------------------")
print(Person.get_person())
print("\nEmployees --------------------------")
print(Employee.get_employee())
print("\nStudents --------------------------")
print(Student.get_student())