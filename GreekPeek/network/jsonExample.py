import json

data = [
{
'name': 'luis',
'phone': '206-478-4652',
'email': 'luisnaranjo733@gmail.com',
'major': 'CSE',
'grade': 'freshman'
},

{
'name': 'michael',
'phone': '206-428-4652',
'email': 'luisnasdfjo733@gmail.com',
'major': 'comm',
'grade': 'freshman'
},
]

serialized = json.dumps(data)

