import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        logger.info(f"Created Employee : {self.fullname}, {self.email}")

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def email(self):
        return f"{self.firstname}.{self.lastname}@email.com"


emp_1 = Employee("Prabhu", "Deva")
emp_2 = Employee("Kamala", "Kannan")
