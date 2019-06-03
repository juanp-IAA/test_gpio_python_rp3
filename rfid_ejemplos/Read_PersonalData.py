#!/usr/bin/env python

import signal
import time
import sys

from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

        print("Setting tag")
        if not rdr.select_tag(uid):
        	print("\nAuthorizing")
        #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
        #util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
		if not rdr.card_auth(rdr.auth_a, 4 , [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
        		print("\nReading")
			name = rdr.read(4)
			print ("Name:" + ''.join(chr(i) for i in name[1]) )
			#print("Reading personal data:\n Name: " + str(rdr.read(4)))
        		#util.read_out(4)
		if not rdr.card_auth(rdr.auth_a, 1 , [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
			surname = rdr.read(1)
			print ("Apellido:"  + ''.join(chr(i) for i in surname[1]) )
			#print("Surname: " + str(rdr.read(1)))

        print("\nDeauthorizing")
        rdr.stop_crypto()
        time.sleep(1)

	rdr.cleanup()

