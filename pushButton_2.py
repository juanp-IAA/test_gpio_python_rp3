#!/usr/bin/env python


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_UP)

print('Press the button.')
while True:
     input_state = GPIO.input(22)
     if input_state == False:
             print('Button Pressed.')
             time.sleep(0.2)

