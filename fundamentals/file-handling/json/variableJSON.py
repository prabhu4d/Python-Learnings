"""
 Corey Schefar  https://youtu.be/9N6a-VLBa2I

"""

import json

personJSON = '''
{
  "person" : [{
                "name": "prabhu",
                "email": "prabhu@gmail.com"
              },
              {  
                "name":"ammu",
                "email": "ammu@gmail.com"
              }
             ],
  "contact" : "8610694983"
}
'''

person = json.loads(personJSON)
print(person)

del person['contact']
new_person = json.dumps(person, indent=2, sort_keys=True)
print(new_person)
