import requests
import json

url = "https://whispersms.xyz/api/send_transactional_message_plain_placeholders/"

def send_sms(phone, heart_rate, lng, lat):

    payload = json.dumps({
    "receiver": phone,
    "template": "b4cf3f53-85b1-45c1-b677-3de6d55309b5",
    "lat": lat,
    "lng": lng,
    "bpm": heart_rate
    })
    headers = {
    'Authorization': 'Api_key gAAAAABiPeU1O4dNGzd2R596_UrxU_xPvFLo8jX263EGGhEBdDZ8sjg7X8UBpeLRKFAwLb55OvXWWxTkXZbTiWo2FFTLpQc-AmypjJc7zpfehSSC1ZJC-Lunu94GkzpiM9Sqfqlt7OR2DPaCgu5zsHzGYlVVJ8bKxA==',
    'Content-Type': 'application/json',
    'Cookie': 'csrftoken=wfA6Xo17ny2tDJAn1HvIAHcCu7Vubwda77jfmSYeFFnYwrXJdL5MqyINSFkNxRoo; sessionid=xccq3f91cc0vlnj2ctmmdycdsrfua7p6'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
# phone = input("Enter phone : ")
# send_sms(phone)