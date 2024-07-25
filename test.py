import requests
payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
header = {
            "Content-Type": "application/json"
         }
response = requests.post("https://restful-booker.herokuapp.com/booking", json=payload , headers=header)
print(response.text)