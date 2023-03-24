import requests
import json

value=""
def getUser(userid):
    url="https://jsonplaceholder.typicode.com/users?id=" +str(userid)
    get_user=(requests.get(url))
    data=get_user.json()
    asstring=json.dumps(data,indent=3)
    # if value in asstring:
    #     print("{} is present in the response".format(value))
    print(asstring)
    assert get_user.status_code,200
    user_name=data[0]['name']
    print(data[0]['name'])
    # if user_name=="Leanne Graham":
    #     print("success")
    assert user_name,"Graham"

getUser(1)





