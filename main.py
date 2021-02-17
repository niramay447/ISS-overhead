import requests
import datetime
import smtplib
MY_LAT = 23.064740
MY_LNG = 70.129860
MY_EMAIL = example@email.com
MY_PASSWORD = ExamplePassword


def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json#")

    response.raise_for_status()

    data = response.json()


    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude= float(data["iss_position"]["latitude"])

    iss_position = (longitude,latitude)

    #your position is within +5 or -5 degrees of the ISS position

        if MY_LAT-5<= iss_latitude <= MY_LAT+5 and MY_LNG-5<=iss_longitude<=MY_LNG:
            return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now<= sunrise:
        return True


if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="SUbject:Look Up \n\n The ISS is above you in the sky"
    )
