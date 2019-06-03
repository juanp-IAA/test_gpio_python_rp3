import RPi.GPIO as GPIO
import time
 
# Use physical pin numbers
GPIO.setmode(GPIO.)
# Set up header pin xx (GPIOx) as an output
print "Setup Pin "
GPIO.setup(xx, GPIO.OUT)
 
var=1
print "Start loop"
while var==1 :
  print "Set Output False"
  GPIO.output(xx, False)
  time.sleep(1)
  print "Set Output True"
  GPIO.output(xx, True)
  time.sleep(1)

