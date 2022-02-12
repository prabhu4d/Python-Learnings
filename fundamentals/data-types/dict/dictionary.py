"""
Dict is similar to List
list is accessed by index value.

Dict it is accessed by key
Dict holds key and value

"""
import pprint

dic = {'name': 'Prabhu', 'age': 20, 'profession': 'AI engineer'}

print(dic['name'])

# copy

d = dic
print(d)

d1 = dic.copy()
print(d)

# update
dic.update({'revenue': '100B/year'})
print(dic)

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("Students Name: %s" % list(Dict.items()))

st = Dict.keys()
print(st)

dic1 = {1: "One", 2: "Two", 4: "Four"}
print(dic1[1])
print(dic1.get(3, "Not Found 🟧"))

# Creating Dict with List
keys = ['Prabhu', 'Rabiya', 'Vignesh']
values = ['JavaScript', 'Python', 'Java']

programmingLoves = dict(zip(keys, values))
print(programmingLoves)

# list, dict in dict
ide = {
    "python": ["Sublime", "Atom", "VS code"],
    "JS": "Atom",
    "C#": "Visual Studio",
    "Java": {
        "JSE": "Netbeans",
        "JEE": "Eclipse"
    }
}

pp = pprint.PrettyPrinter(indent=2)

pp.pprint(ide)
