import requests
import json

URL = "http://127.0.0.1:8000/studentadd/"

data = {
    'firstname':'SAMPLE',
    'lastname':'SAMPLELASTNAME',
    'email':'asd@gmail.com',
    'password':'123456',
    'contact':'123456789',
    'city':'city',
}

json_data = json.dumps(data)
res = requests.post(url = URL, data = json_data)
data = res.json()
print(data)