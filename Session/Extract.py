import requests
import json
req=requests.get("http://api.dailysmarty.com/posts")
received=req.json()
k=((received['posts'][1]))
print(type(k))
# received=json.dumps(k,indent=2)
# print(received)
# print(type(received))
# t=json.load(received)
# print("The type of t is", type(t))
# f=open("E:\\textfile.txt",'w')
# f.write(k)
# f.close()
