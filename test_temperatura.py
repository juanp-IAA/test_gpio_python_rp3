# -*- coding: utf-8 -*-

def get_temp_sens():
        tfile = open("/sys/bus/w1/devices/28-01162e4dc4ee/w1_slave")
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return float(temperature)

mensaje = str(get_temp_sens()) + "C"

print(mensaje)

