from utils.jsonreadhelper import Json_reader
from helper.request_api import APIrequests
from endpoints_api.all_apis_endpoints import Endpoints
from data.payloads.create_new_user_data import Payload

class Test_API:
    """
    Test suite for API endpoints including various HTTP methods.
    """

    def test_01_get_single_userdata(self):
        """Tests GET request for single user data and validates the response schema."""
        response = APIrequests.get_api(f"{Endpoints.URL_SINGLE_USER_API}")
        print(response.json())
        Json_reader.validate_schema("valid_getApi_single_user_schema.json", response.json())

    def test_02_post_new_user(self):
        """Tests POST request for creating a new user and validates the response schema."""
        payload = Payload.new_user("piyush", "QA Automation Tester")
        response = APIrequests.post_api(f"{Endpoints.URL_CREATE_NEW_USER}", payload)
        print(response.json())
        Json_reader.validate_schema("valid_postApi_create_new_user_schema.json", response.json())
        assert response is not None
        assert response.status_code == 201

    def test_03_put_data(self):
        """Tests PUT request for updating user details and validates the response schema."""
        payload = Payload.update_user_details("Pravin", "QA tester")
        response = APIrequests.put_api(f'{Endpoints.URL_UPDATE_EXIST_USER}', payload)
        Json_reader.validate_schema("valid_putApi_update_user_schema.json", response.json())
        assert response.json()['name'] == "Pravin"
        assert response.status_code == 200

    def test_04_delete_data(self):
        """Tests DELETE request for deleting user data and verifies the status code."""
        response = APIrequests.delete_api(Endpoints.URL_DELETE_USER_API)
        assert response.status_code == 204

    def test_05_unknown_users(self):
        """Tests GET request for unknown users and validates the response schema."""
        response = APIrequests.get_api(Endpoints.URL_UNKNOWN_USERS_API)
        Json_reader.validate_schema("valid_getApi_unknown_user_schema.json", response.json())
        assert type(response.json()['data'][0]['id']) == int
        assert response.status_code == 200

    def test_06_patch_api(self):
        """Tests PATCH request for partially updating user details and validates the response schema."""
        payload = Payload.update_user_details("Akash", "QA tester")
        response = APIrequests.patch_api(Endpoints.URL_PATCH_SPECFIC_USER_DETAILS, payload)
        Json_reader.validate_schema("valid_patchApi_update_specific_data_schema.json", response.json())
        assert response.status_code == 200

    def test_07_post_register_api(self):
        """Tests POST request for registering a new user and validates the response schema."""
        payload = Payload.register_new_user("eve.holt@reqres.in", "pistol")
        response = APIrequests.post_api(Endpoints.URL_POST_REGISTER_API, payload)
        Json_reader.validate_schema("valid_postApi_register_new_user.json", response.json())
        assert response.status_code == 200

    def test_08_post_unsuccessful_register_api(self):
        """Tests POST request for an unsuccessful user registration and validates the response schema."""
        payload = Payload.register_new_user("eve.holt@reqres.in", "")
        response = APIrequests.post_api(Endpoints.URL_POST_REGISTER_API, payload)
        Json_reader.validate_schema("valid_postApi_unsuccses_register_schema.json", response.json())
        assert response.status_code == 400

    def test_09_post_api_login(self):
        """Tests POST request for user login and validates the response schema."""
        payload = Payload.login_payload()
        response = APIrequests.post_api(Endpoints.URL_LOGIN_USER, payload)
        Json_reader.validate_schema("valid_postApi_login_user_schema.json", response.json())
        assert response.status_code == 200

    def test_10_delay_response(self):
        """Tests delay response API by validating JSON schema and checking status code 200."""
        response = APIrequests.get_api(Endpoints.URL_DELAY_RESPONSE)
        print(response.json())
        Json_reader.validate_schema("valid_getApi_delay_response_schema.json", response.json())
        assert response.status_code == 200
