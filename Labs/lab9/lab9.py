import json
import requests
r = requests.get('http://localhost:3000')

data = r.json()
i = 0
for x in data:
    widgetX = data[i] 
    print(f"{widgetX['name']} is {widgetX['color']}")
    i = i+1
