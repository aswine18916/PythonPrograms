import requests
import json
import jsonpath


"""Reading  a request from an API using get method.
 Fetching a particular node from the output.
 Writing the fetched output to a text file"""

req=requests.get("http://api.dailysmarty.com/posts")
received=req.json()
print(received)
# for each in received ['posts']:
#     print(each['title'])


# utilities = "https://jsonplaceholder.typicode.com/users?id=" + str(userid)
# get_user = (requests.get(utilities))