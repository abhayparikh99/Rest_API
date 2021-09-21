import requests
import json

URL = "http://127.0.0.1:8000/studentUpdate/"

data = {
    'id':2,
    'firstname':'DJANGO',
    'lastname':'FRAMEWORK',
    'email':'dj@gmail.com',
    'password':'45456',
    'contact':'1111444',
    'city':'Ahmedabad',
}

json_data = json.dumps(data)
res = requests.put(url = URL,data = json_data)
data = res.json()
print(data)