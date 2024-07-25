import requests
from requests import RequestException
from utils.generate_logs import Loggen
class APIrequests:
    logs = Loggen.logger()

    @staticmethod
    def get_api(url, header=None):
        """Sends a GET request and logs the URL and response."""
        if header is None:
            header = {}
        try:
            response = requests.get(url, header)
            APIrequests.logs.info(f"URL:----{url} and Response:----{response}")
            return response
        except RequestException as R:
            APIrequests.logs.error(f"Exception Occure:---{R}")

    @staticmethod
    def post_api(url, payload, header={}):
        """Sends a POST request and logs the URL, payload, and headers."""
        try:
            response = requests.post(url, json=payload, headers=header)
            APIrequests.logs.info(f"URL:----{url} data_payload:----{payload} header:----{header}")
            return response
        except RequestException as R:
            APIrequests.logs.error(F"Exception Occure:----{R}")

    @staticmethod
    def put_api(url, payload, header={}):
        """Sends a PUT request and logs the URL, payload, and headers."""
        try:
            response = requests.put(url, data=payload, headers=header)
            APIrequests.logs.info(f"URL:----{url} data_payload:----{payload} header:----{header}")
            return response
        except RequestException as R:
            APIrequests.logs.error(F"Exception Occure:----{R}")

    @staticmethod
    def delete_api(url):
        """Sends a DELETE request and logs the URL and response."""
        try:
            response = requests.delete(url)
            APIrequests.logs.info(f"URL:----{url} and Response:----{response}")
            return response
        except RequestException as R:
            APIrequests.logs.error(F"Exception Occure:----{R}")

    @staticmethod
    def patch_api(url, payload, header={}):
        """Sends a PATCH request and logs the URL, payload, and headers."""
        try:
            response = requests.patch(url, data=payload, headers=header)
            APIrequests.logs.info(f"URL:----{url} and Response:----{response}")
            return response
        except RequestException as R:
            APIrequests.logs.error(F"Exception Occure:----{R}")









