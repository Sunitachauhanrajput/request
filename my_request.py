import requests
import json
from requests.api import options
result=requests.get('http://saral.navgurukul.org/api/courses/74/exercises')
data=result.json()
with open("data.json","w")as f:
    json.dump(data,f,indent=4)
print(result)


