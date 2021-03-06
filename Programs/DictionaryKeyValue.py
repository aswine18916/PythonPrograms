import json
"""Creating a dictionary and Accessing the items in the dictionary"""
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
for k, v in x.items():
    if k == "married":
        print(v)
print(x["cars"][0]["model"])

fp=json.dumps(x["cars"][0])
print(fp)
