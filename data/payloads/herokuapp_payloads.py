class Herokuapp_payload:

    @staticmethod
    def create_new_booking_payload(name,lname,price):
        return {
    "firstname" : f"{name}",
    "lastname" : f"{lname}",
    "totalprice" : f"{price}",
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    @staticmethod
    def insert_new_data_in_existing_user():
        return {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

