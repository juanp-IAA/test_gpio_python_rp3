#!/usr/bin/env python


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD ) # BCM or BOARD
GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP)

print('Press the button.')
while True:
     input_state = GPIO.input(15)
     if input_state == False:
             print('Button Pressed.')
             time.sleep(0.2)

