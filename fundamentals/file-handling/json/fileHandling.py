import json

filePath = 'todos.json'

with open(filePath) as file:
    data = json.load(file)

for todo in data['todos']:
    todo['completed'] = True
    todo['title'] = todo['title'].upper()

with open('completed_todos.json', 'w') as file:
    json.dump(data, file, indent=2)
