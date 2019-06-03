import RPi.GPIO as GPIO
import time
 
# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin  (GPIO13) as an output
print "Setup Pin " # El led verde 
GPIO.setup(xx, GPIO.OUT)

GPIO.setup(xx, GPIO.IN,pull_up_down=GPIO.PUD_xx)

 
var=1
print "Start loop"
while var==1 :
  print "Set Output False"
  GPIO.output(xx, False)
  time.sleep(1)
  if GPIO.input(xx)== 0:
    print "Set Output False"
    GPIO.output(xx, False)
  else:
    print "Set Output True"
    GPIO.output(xx, True)

  time.sleep(1)
