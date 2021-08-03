import requests
import json

req=requests.get("http://api.dailysmarty.com/posts")
received=req.json()
#print(received['posts'][1]['title'])
k=((received['posts'][1]['title']))
#print(k)
f=open("E:\\textfile.txt",'w')
f.write(k)
f.close()
print("Added the string")

