import json
from jsonschema import validate, ValidationError
from utils.jsonreadhelper import Json_reader
from helper.request_api import APIrequests
from utils.config import BASE_URL
from endpoints_api.all_apis_endpoints import Endpoints
import json
from data.payloads.create_new_user_data import Payload
class Test_API:

    def test_01_get_single_userdata(self):
        response = APIrequests.get_api(f"{BASE_URL}{Endpoints.SINGLE_USER_API}")
        print(response.json())
        json_data = response.json()
        print(response.json()['data']['id'])
        with open("/Users/user/PycharmProjects/API_personal_framework/piyush_apis_framework/schema/valid_getApi_single_user_schema.json", 'r') as schema_file:
            schema = json.load(schema_file)
        validate(instance=response.json(), schema=schema)
        id = type(response.json()['data']['id'])
        assert  id == int

    def test_02_post_new_user(self):
        payload = Payload.new_user("piyush","QA Automation Tester")
        response = APIrequests.post_api(f"{BASE_URL}{Endpoints.CREATE_NEW_USER}", payload)
        print(response.json())
        assert response is not None
        assert response.status_code == 201

    def test_03_put_data(self):
        payload = Payload.update_user_details("Pravin", "QA tester")
        response = APIrequests.put_api(f'{BASE_URL}/users/2', payload)
        print(response.json())
        assert response.json()['name'] == "Pravin"
        assert response.status_code == 200