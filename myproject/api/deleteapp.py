import requests
import json

URL = "http://127.0.0.1:8000/studentDelete/"

data = {
    'id':5,
}

json_data = json.dumps(data)
res = requests.delete(url = URL,data = json_data)
data = res.json()
print(data)