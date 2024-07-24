class Payload:

    @staticmethod
    def new_user(names, job_profile):
        return {"name": f"{names}", "job": f"{job_profile}"}

    @staticmethod
    def update_user_details(names, job_profile):
        return   {"name": f"{names}", "job": f"{job_profile}"}