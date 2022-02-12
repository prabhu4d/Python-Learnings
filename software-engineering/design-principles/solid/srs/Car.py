"""
Single Responsibility Principle

* A class should only have one primary responsibility
* A class should have only one reason to change
* if secondary responsibe

1. Car have responsible to start, run, stop, change speed - Primary Responsible
2. Car -> Parking, Washing  - Secondary Responsibile

"""


class Car:
    def __init__(self, name):
        self.name = name
        self.running = False
        self.started = False
        self.gear = 1

    def start(self):
        self.started = True
        return "Started"

    def run(self):
        self.running = True
        return "Running"

    def stop(self):
        self.started = False
        self.running = False
        return "Stopped"

    def brake(self):
        self.running = False
        return "Brake"

    def change_gear(self, gear):
        self.gear = gear
        return "Gear Changed"

    def __str__(self):
        if self.running:
            return f"{self.name} is running at {self.gear}"
        elif self.stop:
            return f"{self.name} in off"
        else:
            return f"{self.name} is started"


class Parking:
    def __init__(self, location):
        self.location = location
        self.parkedVehicles = []

    def park(self, vehicle):
        vehicle.stop()
        self.parkedVehicles.append(vehicle)

    def __str__(self):
        vechilesList = "Parked Vehicles are\n"
        for vehicle in self.parkedVehicles:
            vechilesList += f"{vehicle.name}\n"

        return vechilesList


class Washing:
    def __init__(self, location):
        self.location = location

    def wash(self, vehicle):
        return f"{vehicle.name} washed successfully"


cars = [Car("Audi"), Car("Tata"), Car("Skoda")]
park = Parking("Coimbatore Railway Station")


def runCar(car):
    car.start()
    car.run()
    car.change_gear(3)


for car in cars:
    runCar(car)
    print(car)

for car in cars:
    park.park(car)
print(park)

CarCare = Washing("Kovai")
print(CarCare.wash(Cars[0]))
