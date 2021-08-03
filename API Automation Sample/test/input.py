import requests
import json
response=requests.get("http://api.dailysmarty.com/posts")
assert response.status_code==200
print("True")