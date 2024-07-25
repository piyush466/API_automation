import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class Endpoints:
    """
    Endpoints class for storing API endpoint URLs.

    This class contains constants for various API endpoints used in the test cases.
    Each constant represents a specific API endpoint URL.
    """

    BASE_URL = os.getenv("url")
    """Base URL for the API."""

    URL_SINGLE_USER_API = BASE_URL + "/users/2"
    """Endpoint URL for getting single user data."""

    URL_CREATE_NEW_USER = BASE_URL + "/users"
    """Endpoint URL for creating a new user."""

    URL_UPDATE_EXIST_USER = BASE_URL + "/users/2"
    """Endpoint URL for updating an existing user's details."""

    URL_DELETE_USER_API = BASE_URL + "/users/2"
    """Endpoint URL for deleting a user."""

    URL_UNKNOWN_USERS_API = BASE_URL + "/unknown"
    """Endpoint URL for getting data of unknown users."""

    URL_PATCH_SPECFIC_USER_DETAILS = BASE_URL + "/user/2"
    """Endpoint URL for partially updating specific user details."""

    URL_POST_REGISTER_API = BASE_URL + '/register'
    """Endpoint URL for registering a new user."""

    URL_LOGIN_USER = BASE_URL + "/login"
    """Endpoint URL for user login."""

    URL_DELAY_RESPONSE = BASE_URL + "/users?delay=2"
