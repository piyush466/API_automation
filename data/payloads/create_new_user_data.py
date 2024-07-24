class Payload:

    @staticmethod
    def new_user(names, job_profile):
        return {"name": f"{names}", "job": f"{job_profile}"}