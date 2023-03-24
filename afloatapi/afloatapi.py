import requests
import json

req=requests.get("https://api.publicapis.org/entries")
print(json.dumps(req.json(),indent=4))
# k=((received['posts'][1]['title']))
# #print(k)
# f=open("E:\\textfile.txt",'w')
# f.write(k)
# f.close()
# print("Added the string")

