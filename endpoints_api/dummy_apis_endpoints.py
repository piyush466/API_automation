import os
from dotenv import load_dotenv
load_dotenv()
class DummyEndpoints:

    BASE_URL = os.getenv("Dummyurl")

    #get all user data and its api end point
    URL_ALL_USER_DATA = BASE_URL + "/booking"

