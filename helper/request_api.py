import requests
from requests import RequestException

class APIrequests:

    @staticmethod
    def get_api(url):
        try:
            response = requests.get(url)
            return response
        except RequestException as R:
            print("Exception Occure",  R)

    @staticmethod
    def post_api(url,payload,header={}):
        try:
            response = requests.post(url, data=payload, headers=header)
            return response
        except RequestException as R:
            print("exception Occure", R)

    @staticmethod
    def put_api(url,payload,header={}):
        try:
            response = requests.put(url,data=payload,headers=header)
            return response
        except RequestException as R:
            print("exception Occure", R)

    @staticmethod
    def delete_api(url):
        try:
            response = requests.delete(url)
            return response
        except RequestException as R:
            print("exception Occure", R)









