"""
> Passing Mutable Data Types reference

"""


fruits_list = ["Apple"]
print("Address of Fruits List : ", id(fruits_list))


def add_fruit(fruits_container, fruit_name):
    print("Address of Fruits_Container : ", id(fruits_container))
    fruits_container.append(fruit_name)
    print("Inside", fruits_container)


add_fruit(fruits_list, "Pine Apple")
print("Outside", fruits_list)
