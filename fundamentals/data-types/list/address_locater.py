"""

Checking the order

"""


def size(a):
    return a.__sizeof__()


def element_address(li):
    last_ele_add = id(li[0])
    for ele in li:
        address = id(ele)
        print(
            f"Address : {address}, Size: {size(ele)}, difference: {address - last_ele_add}")
        last_ele_add = address


name = ["Prabhu", "Kumaran", "Priyanka", "Rabiya", "Kannan"]

print(f"""
Size: {size(name)}
Address: {id(name)} 
""")

element_address(name)
