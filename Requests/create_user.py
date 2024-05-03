import requests
import json
import jsonpath
url = "https://reqres.in/api/users"
file = open('C:\\Sadiq\\create_user.json', 'r')
json_input = file.read()
json_request = json.loads(json_input)
response = requests.post(url,json_request)
json_response = json.loads(response.text)
id = jsonpath.jsonpath(json_response, 'id')
print(id[0])

