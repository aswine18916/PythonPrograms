"""Opening a text file
Reading the contents of the file.
Converting the contents in the text to a python dictionary"""

import json

f=open("textfile.txt","r")
k=f.read()
print(k)
t=json.loads(k)
print(t["name"])
print(type(t))


