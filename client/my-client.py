import requests, json

response = requests.get('http://127.0.0.1:5000/retrieve')
item = json.loads(response.text)

for each in item["data"]:
    print(each)