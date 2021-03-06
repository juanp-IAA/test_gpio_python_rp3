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
        		print("\nWRite the Card.")
			name = rdr.write(4, [0x57, 0x65, 0x6c, 0x63, 0x6f, 0x6d, 0x65, 0x20, 0x74, 0x6f, 0x20, 0x52, 0x50, 0x49, 0x21, 0x21])

		#if not rdr.card_auth(rdr.auth_a, 4 , [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
			#mensaje = rdr.read(4)
			#print ("Mesaje:"  + ''.join(chr(i) for i in mensaje[1]) )

        print("\nDeauthorizing")
        rdr.stop_crypto()
        time.sleep(1)

	rdr.cleanup()

