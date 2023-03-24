import requests
from APIAutomationSample import test
import json
# response=requests.get("http://api.dailysmarty.com/posts")
# print(response.status_code)
# assert response.status_code==200
# print("True")
with open(".././url/base_url.json") as apifile:
    convert_to_json=  json.loads(apifile.read())
    api_value=convert_to_json["utilities"]
    print(api_value)

with open(".././data/checkdata.json") as datafile:
    valueread=datafile.read()
    final=(json.loads(valueread))
    print(final["posts"][0]["id"])

# value=requests.get(api_value)P

