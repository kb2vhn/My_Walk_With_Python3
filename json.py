# John wood
# Aug 31, 2020
# this example is on freecodecamp

# JSON
import json
data = '''{
    "name":"chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
        "email" :{
            "hide" : "yes"
            }
            }'''
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

print('\n')

inp = '''[
    { "id" : "023",
      "x" : "43",
      "name": "John"
    },
    {
         "id" : "323",
        "x" : "431",
        "name": "Jon"
    }
]'''

info = json.loads(inp)
print('user count:', len(info))
for item in info:
    print('name', item['name'])
    print('id', item['id'])
    print('att', item["x"])

