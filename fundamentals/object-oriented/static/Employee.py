class Employee:
    ceo = "Boss"

    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def show(self):
        print(f"{self.id} : {self.salary} : {Employee.ceo}")

    def showSelf(self):
        print(f"{self.id} : {self.salary} : {self.ceo}")


# Static CEO
prabhu = Employee(1, 10000)
ammu = Employee(2, 20000)
prabhu.show()
ammu.show()

# Instance CEO
print(f"\nceo of ammu {ammu.ceo}")
ammu.ceo = "Leader"
print(f"ceo of ammu {ammu.ceo}")
print(f"Employee CEO {Employee.ceo}")

print("\n")
prabhu.showSelf()
ammu.showSelf()

prabhu.name = "Prabhu"
