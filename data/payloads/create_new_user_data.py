class Payload:

    @staticmethod
    def new_user(names, job_profile):
        """Generates a dictionary with 'name' and 'job' for a new user."""
        return {"name": f"{names}", "job": f"{job_profile}"}

    @staticmethod
    def update_user_details(names, job_profile):
        """Generates a dictionary with updated 'name' and 'job' for a user."""
        return {"name": f"{names}", "job": f"{job_profile}"}

    @staticmethod
    def register_new_user(email, password):
        """Generates a dictionary with 'email' and 'password' for registration."""
        return {"email": f"{email}", "password": f"{password}"}

    @staticmethod
    def login_payload():
        """Generates a dictionary with predefined 'email' and 'password' for login."""
        return {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
