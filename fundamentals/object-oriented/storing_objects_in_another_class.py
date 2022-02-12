"""
What is the use of storing objects in another class

asked by Kannan

"""


class Sky:
    cloud = []

    @classmethod
    def rain(cls, ocean):
        for i in cls.cloud:
            print("💧", i)
            ocean.waterdrops += 1
        cls.cloud = []

    @classmethod
    def cloud_details(cls):
        return f"I have {len(cls.cloud)} vapours"


class Sea:
    def __init__(self, waterdrops):
        self.waterdrops = waterdrops

    def vapour(self, waterdrops):
        waterdrops = waterdrops if waterdrops < self.waterdrops else self.waterdrops
        for i in range(waterdrops):
            self.waterdrops -= 1
            Vapour(i)

    def __str__(self):
        return f"I have {self.waterdrops} waterdrops"


class Vapour:
    def __init__(self, drop_number):
        self.drop_number = drop_number
        Sky.cloud.append(self)

    def __str__(self):
        return f"Drop {self.drop_number}"


# Indian Ocean
indian_ocean = Sea(10000)
print(indian_ocean)

# Water Vapouring
print(Sky.cloud_details())
indian_ocean.vapour(100)
print(indian_ocean)

print(Sky.cloud_details())
Sky.rain(indian_ocean)
print(Sky.cloud_details())
print(indian_ocean)
