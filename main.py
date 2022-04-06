from app import record_audio
from heart import checkheart_rate
from lcd import mylcd
from gpio import watch_gpio
from gps import get_gps_data
from gclouds import upload_to_bucket
from sms import send_sms
from time import sleep
from datetime import datetime

RECIPIENT_NUMBER = "2348031346306"
display = mylcd.text

while True: # Run program for ever
  
  display("Watching Button press", 1)
  watch_gpio() # Keep checking until button is pressed
  
  display("Checking Heart_rate", 1)
  heart_rate = int(checkheart_rate())
  
  display(f"Fetching Gps", 2)
  lng, lat = get_gps_data()

  
  display("Recording Audio", 1)
  audio_file = record_audio()
  
  display("Uploading Audio", 1)
  upload_to_bucket(f"{int(datetime.now().timestamp())}.wav)", audio_file)
  display("Uploaded", 2)
  
  send_sms(RECIPIENT_NUMBER, heart_rate, lng, lat)