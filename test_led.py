import RPi.GPIO as GPIO
import time
 
# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 29 (GPIO5) as an output
print "Setup Pin "
GPIO.setup(29, GPIO.OUT)
 
var=1
print "Start loop"
while var==1 :
  print "Set Output False"
  GPIO.output(29, False)
  time.sleep(1)
  print "Set Output True"
  GPIO.output(29, True)
  time.sleep(1)

