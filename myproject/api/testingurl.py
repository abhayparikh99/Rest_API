import requests

URL = "http://127.0.0.1:8000/api/getall/"

r = requests.get(url=URL)
data = r.json()
print("Type of data = ",type(data))
print(data)
