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
        response = APIrequests.get_api(f"{Endpoints.URL_SINGLE_USER_API}")
        print(response.json())
        Json_reader.validate_schema("valid_getApi_single_user_schema.json", response.json())

    def test_02_post_new_user(self):
        payload = Payload.new_user("piyush","QA Automation Tester")
        response = APIrequests.post_api(f"{Endpoints.URL_CREATE_NEW_USER}", payload)
        print(response.json())
        Json_reader.validate_schema("valid_postApi_create_new_user_schema.json", response.json())
        assert response is not None
        assert response.status_code == 201

    def test_03_put_data(self):
        payload = Payload.update_user_details("Pravin", "QA tester")
        response = APIrequests.put_api(f'{Endpoints.URL_UPDATE_EXIST_USER}', payload)
        Json_reader.validate_schema("valid_putApi_update_data_schema.json", response.json())
        assert response.json()['name'] == "Pravin"
        assert response.status_code == 200

    def test_04_delete_data(self):
        response = APIrequests.delete_api('https://reqres.in/api/users/2')
        assert response.status_code == 204