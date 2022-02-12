from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, email, location):
        self.name = name
        self.age = age
        self.email = email
        self.location = location

    @abstractmethod
    def tell_about_yourself(self):
        pass


class Owner(Person):
    __instance = None

    def __init__(self, name, age, email, location, company):
        if Owner.__instance != None:
            raise Exception("You can create only one owner")
        else:
            super().__init__(name, age, email, location)
            self.company = company
            Owner.__instance = self

    def tell_about_yourself(self):
        print(f"""
        Hi I'm {self.name},
        I Own a company called {self.company}
        """)

    def __str__(self):
        return f"""
        Name    : {self.name}
        Age     : {self.age}
        Email   : {self.email}
        Location: {self.location}
        Company : {self.company}
        """


class Employee(Person):
    __employees = []

    def __init__(self, name, age, email, location, team=None):
        super().__init__(name, age, email, location)
        self.team = team
        Employee.__employees.append(self)

    def tell_about_yourself(self):
        print(f"""
        Hi I'm {self.name},
        My Team is {self.team.name}
        """)

    @classmethod
    def details(cls):
        for emp in cls.__employees:
            print(f"""
            Name : {emp.name}
            Team : {emp.team.name}
            """)

    def __str__(self):
        return f"""
        Name    : {self.name}
        Age     : {self.age}
        Email   : {self.email}
        Location: {self.location}
        Team : {self.team.name}
        """


class Client(Person):
    __clients = []

    def __init__(self, name, age, email, location, company):
        super().__init__(name, age, email, location)
        self.company = company
        self.projects = []
        Client.__clients.append(self)

    def tell_about_yourself(self):
        print(f"""
        Hi I'm {self.name},
        from {self.location},
        My Company is {self.company}
        """)

    @classmethod
    def details(cls):
        for client in cls.__clients:
            print(f"""
            Name: {client.name}
            Company: {client.company}
            Projects: {[project.name for project in client.projects]}
            """)

    def __str__(self):
        return f"""
        Name    : {self.name}
        Age     : {self.age}
        Email   : {self.email}
        Location: {self.location}
        Company : {self.company}
        """
