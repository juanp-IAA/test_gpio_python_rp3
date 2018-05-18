import RPi.GPIO as GPIO
import time
 
# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 33 (GPIO13) as an output
print "Setup Pin 33" # El led verde 
GPIO.setup(33, GPIO.OUT)

GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP)

 
var=1
print "Start loop"
while var==1 :
  print "Set Output False"
  GPIO.output(33, False)
  time.sleep(1)
  if GPIO.input(15)== 0:
    print "Set Output False"
    GPIO.output(33, False)
  else:
    print "Set Output True"
    GPIO.output(33, True)

  time.sleep(1)
