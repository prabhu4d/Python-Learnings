import time as t
import sys
from math import radians, cos, sin, asin, sqrt


class Map:
    """
    grid is 2d cartesian coordinate to locate the place
    """
    grid = {
        0: {
        },
        1: {
        }
    }

    @classmethod
    def add_place(cls, place):
        try:
            float(place.lat)
            float(place.long)

            if place.lat in cls.grid and place.long in cls.grid[place.lat]:
                raise Exception(
                    f"Place {place} can't be added because {cls.grid[place.lat][place.long]} already exist there")
            if place.lat in cls.grid:
                cls.grid[place.lat][place.long] = place
            else:
                cls.grid[place.lat] = {place.long: place}
        except Exception as e:
            print(e)
            place.update_location()

    @classmethod
    def distance_calculator(cls, source, destination):
        lat1 = radians(source.lat)
        long1 = radians(source.long)
        lat2 = radians(destination.lat)
        long2 = radians(destination.long)

        dlong = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlong / 2)**2

        c = 2 * asin(sqrt(a))
        r = 6371

        return (c * r)

    @classmethod
    def show_places(cls):
        for x in cls.grid:
            for y in cls.grid[x]:
                print(f"({x}, {y}) -> {cls.grid[x][y]}")


class Place:
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        Map.add_place(self)

    def update_location(self):
        self.lat = float(input("Enter New Latitude: "))
        self.long = float(input("Enter New Longitude: "))
        Map.add_place(self)

    def __str__(self):
        return f"{self.name}"


class Vechile:
    def __init__(self, name, rc_no, mileage, top_speed, location=None, petrol=0):
        self.name = name
        self.rc_no = rc_no
        self.mileage = mileage
        self.top_speed = top_speed
        self.location = location
        self.petrol = petrol

    def ride_details(self, average_speed, path):
        distance = 0
        for i in range(len(path)-1):
            distance += Map.distance_calculator(path[i], path[i+1])

        petrol_needed = (distance / self.mileage) - self.petrol

        return {
            'distance': int(distance),
            'time': Vechile.time_formatter((distance / average_speed)*60),
            'petrol': int(petrol_needed)
        }

    @staticmethod
    def time_formatter(time):
        hr = round(time // 60)
        mi = round(time % 60)

        def double_digit(digit):
            return digit if digit//10 != 0 else f'0{digit}'

        return f"{double_digit(hr)}h:{double_digit(mi)}m"

    def start_ride(self, average_speed, path):
        petrol_needed = self.ride_details(average_speed, path)['petrol']
        if self.petrol < petrol_needed:
            print("Fuel Low, please fill the tank")
            self.petrol += float(
                input(f"{petrol_needed - self.petrol} Needed : "))

        if self.petrol >= petrol_needed:
            print(f"Ride Started from {path[0]} to {path[-1]}")
            time = 0
            speed_per_10min = (average_speed / 60)*10
            for i in range(len(path)-1):
                source = path[i]
                destination = path[i+1]
                distance = round(Map.distance_calculator(source, destination))
                arrived = False
                crossed = 0
                print(
                    f"\nFrom {source} to {destination} distance -> {distance}Km")
                distance_from_source = 0
                while not arrived:
                    crossed += speed_per_10min
                    t.sleep(1)
                    time += 10
                    self.location = f'{source}+{round(crossed)}'
                    if crossed > distance:
                        arrived = True
                        self.location = destination
                    print(
                        f"  ⏲️ {Vechile.time_formatter(time)} 🚴 {source} ➡️ {destination} 📍 {self.location}")

            print(f" {destination} Arrived")
        else:
            print(f"Petrol Low {self.petrol}")

    def __str__(self):
        return f"""
        Name  : {self.name}
        RC No : {self.rc_no}
        Mileage : {self.mileage} kmph
        Top Speed : {self.top_speed} kmph
        Petrol Level: {self.petrol} l
        Location : {self.location}
        """


coimbatore = Place("Coimbatore", 11.0168,  76.9558)
salem = Place("Salem", 11.6643, 78.1460)
dharmapuri = Place("Dharmapuri", 12.1211, 78.1582)
hosur = Place("Hosur", 12.7409, 77.8253)
bangalore = Place("Bangalore", 12.9716, 77.5946)

Map.show_places()

pulsar = Vechile("Pulsar 220F", "TN 00 1234", 40, 200)
print(pulsar)

cbe_bge = [coimbatore, salem, dharmapuri, hosur, bangalore]

print(pulsar.ride_details(120, cbe_bge))

pulsar.start_ride(120, cbe_bge)
