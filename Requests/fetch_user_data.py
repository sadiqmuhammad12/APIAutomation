from pprint import pprint
#
# import requests
# import json
# import jsonpath
# url = "https://reqres.in/api/users?page=2"
# response = requests.get(url)
# # pprint(response.content)
# json_response = json.loads(response.content.decode('utf-8'))
#
# # print(json.dumps(json_response, indent=2))
#
# # fetch value using jsonpath
# pages = jsonpath.jsonpath(json_response, 'data')
# print(pages[0][0].get('first_name'))
# display first name

import unittest
import requests
import json


class TestAPI(unittest.TestCase):
    def test_api_request(self):
        url = "https://reqres.in/api/users?page=2"
        response = requests.get(url)

        # Assert that the request was successful
        self.assertEqual(response.status_code, 200)

        # Assert that the response content is in JSON format
        self.assertTrue(response.headers['Content-Type'].startswith('application/json'))

        # Decode the response content and load it as JSON
        json_response = json.loads(response.content.decode('utf-8'))

        # Assert specific properties of the JSON response
        self.assertEqual(json_response['page'], 2)
        self.assertEqual(json_response['total'], 12)

        # Add more assertions as needed based on your API response structure


if __name__ == '__main__':
    unittest.main()
