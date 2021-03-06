import requests


"""Reading  a request from an API using get method,
 Fetching a particular node from the output.
 Writing the fetched output to a text file"""

req=requests.get("http://api.dailysmarty.com/posts")
received=req.json()
k=((received['posts'][1]['title']))
print(k)
f=open("E:\\textfile.txt",'w')
f.write(k)
f.close()

received=req.json()
print(received)