#!/usr/bin/env python


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO. ) # BCM or BOARD
GPIO.setup(xx, GPIO.IN)

print('Press the button.')
while True:
     input_state = GPIO.input(xx)
     if input_state == False:
             print('Button Pressed.')
             time.sleep(0.2)

