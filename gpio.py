import time, datetime
import RPi.GPIO as GPIO
from time import sleep

# Pin definitions
btn_pin = 27

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set BTN pin as input
GPIO.setup(btn_pin, GPIO.OUT)


def watch_gpio(max_minutes = 100):


    while True:

        pin_state = GPIO.input(btn_pin)
        print(GPIO.input(btn_pin))

        if pin_state == 1:

            return True
            
        sleep(0.5)
    
#watch_gpio(5000)