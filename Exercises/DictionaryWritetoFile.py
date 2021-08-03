import json
"""Creating a dictionary and writing the items in the dictionary to a file"""
x = {
    "name": "Mike",
    "age": 40,
    "married": True,
    "divorced": False,
    "children": ("Ron", "Kate"),
    "pets": None,
    "cars": [
        {"model": "BMW 330", "mpg": 18.5},
        {"model": "Ford Escape", "mpg": 20.1}
    ]

}
# use four indents to make it easier to read the result:
y=json.dumps(x, indent=4)
print(type(y))
print(x['cars'][1]["model"])
with open("E:\\textfile.txt", 'a+') as text:
  text.write(y)
  text.close()




