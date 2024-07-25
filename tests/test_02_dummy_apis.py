import json

from data.payloads.herokuapp_payloads import Herokuapp_payload
from helper.request_api import APIrequests
from endpoints_api.dummy_apis_endpoints import DummyEndpoints
from utils.jsonreadhelper import Json_reader
class Test_Dummy_Api:
    booking_id = None

    def test_01_get_api(self):
        response = APIrequests.get_api(DummyEndpoints.URL_ALL_USER_DATA)
        print(response.json())
        Json_reader.validate_schema("valid_getApi_booker.json", response.json())
        assert  type(response.json()[1]['bookingid']) == int
        assert response.status_code == 200

    def test_02_post_api_create_booking(self):
        payload = Herokuapp_payload.create_new_booking_payload("piyush", "dravyakar", 1000)
        response = APIrequests.post_api(DummyEndpoints.URL_ALL_USER_DATA, payload)
        Json_reader.validate_schema("valid_postApi_create_new_booking.json", response.json())
        booking_id = response.json()['bookingid']
        assert response.status_code == 200
        return booking_id

    def test_03_get_api_booking_and_check_the_created_data_is_display_or_not(self):
        booking_id = self.test_02_post_api_create_booking()
        response = APIrequests.get_api(DummyEndpoints.URL_ALL_USER_DATA+f"/{booking_id}")
        Json_reader.validate_schema("valid_getApi_getting_id_and_check_data.json", response.json())
        assert response.status_code == 200

    #This is currently not working
    # def test_04_update_the_data_using_id(self):
    #     booking_id = self.test_02_post_api_create_booking()
    #     payload = Herokuapp_payload.insert_new_data_in_existing_user()
    #     response = APIrequests.put_api(DummyEndpoints.URL_ALL_USER_DATA+f"/{booking_id}", payload)
    #     print(response.json())


















