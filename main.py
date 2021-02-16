import requests
MY_LAT = 23.064740
MY_LONG = 70.129860
# response = requests.get(url="http://api.open-notify.org/iss-now.json#")
#
# response.raise_for_status()
#
# data = response.json()
#
#
# longitude=data["iss_position"]["longitude"]
# latitude= data["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)

parameters = {
    "lat": MY_LAT
    "long": MY_LONG

}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()