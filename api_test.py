import requests
import pytest
import json

url = "http://localhost:5000/api/members"
content = {
     "name" : "ajed",
     "email" : "abc@naver.com"
}

def test_get_locations_check_status_code_equals_200():
     print('dd')
     response = requests.get(url)
     assert response.status_code == 200

def test_data_check():
     print('fff')
     response = requests.get(url)
     dic = json.loads(response.text)
     assert [a["name"]for a in dic][0] == 'test1'

def test_create_member():
     response_post = requests.post(url, content)
     response_get = requests.get(url)
     dic = json.loads(response_get.text)     
     assert response_post.status_code == 200 and dic[len(dic)-1]['name'] == content['name']

#how to use
#python3 -m pytest api_test.py