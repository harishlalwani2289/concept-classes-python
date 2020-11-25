import json

with open('cardData.json') as f:
  data = json.load(f)
print(data[1]["data"]["pi"])
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for element in data[1]["data"]["pi"]:
    if(element):
        print(element["name"], end=" : ")
        print(element["cards"])