#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
import datetime

# LED strip configuration:
LED_COUNT      = 29      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#idovel kapcsolatos beallitasok
now=datetime.datetime.now()
sec=now.strftime("%S")
josec=int(sec)

# Define functions which animate LEDs in various ways.
# Esti: 22:00:00-23:59:59 (40-49 sec)
def Esti(strip, color, wait_ms=100):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Delutani: 18:00:00-21:59:59 (30-39 sec)
def Delutani(strip, color, wait_ms=70):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
# Delelotti: 10:00:00-11:59:59 (10-19 sec)
def Delelotti(strip, color, wait_ms=70):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Reggeli: 8:00:00-9:59:59 (00-09 sec)
def Reggeli(strip, color, wait_ms=70):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Napkozi: 12:00:00-15:59:59 (20-29 sec)
def Napkozi(strip, color, wait_ms=70):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Ejszakai: 00:00:00-07:59:59(50-59 sec)
def Ejszakai(strip, color, wait_ms=20):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Nyomjon Ctrl-c kombinaciot a lekapcsolashoz!')


    try:

        while True:
            if(josec>=50 and josec<=59):
                print ('Esti feny')
                Esti(strip, Color(100, 100, 20))
                now=datetime.datetime.now()
                sec=now.strftime("%S")
                josec=int(sec)
                print(now.strftime("%H:%M:%S"))
                print (josec)
                

            elif(josec>=30 and josec<=39):
                print ('Napkozi feny')
                Napkozi(strip, Color(250, 250, 250))
                now=datetime.datetime.now()
                sec=now.strftime("%S")
                josec=int(sec)
                print(now.strftime("%H:%M:%S"))
                print (josec)

            elif(josec>=20 and josec<=29):
                print('Delelotti feny')
                Delelotti(strip, Color(200, 200, 200))
                now=datetime.datetime.now()
                sec=now.strftime("%S")
                josec=int(sec)
                print(now.strftime("%H:%M:%S"))
                print (josec)

            elif(josec>=10 and josec<=19):
                print('Reggeli feny')
                Reggeli(strip, Color(160, 160, 180))
                now=datetime.datetime.now()
                sec=now.strftime("%S")
                josec=int(sec)
                print(now.strftime("%H:%M:%S"))
                print (josec)

            elif(josec>=40 and josec<=49):
                print('Delutani feny')
                Delutani(strip, Color(220, 220, 220))
                now=datetime.datetime.now()
                sec=now.strftime("%S")
                josec=int(sec)
                print(now.strftime("%H:%M:%S"))
                print (josec)

            elif(josec>=0 and josec<=9):
                print('Ejszakai feny')
                Ejszakai(strip, Color(10, 10, 10))
                now=datetime.datetime.now()
                sec=now.strftime("%S")
                josec=int(sec)
                print(now.strftime("%H:%M:%S"))
                print (josec)

            

                


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
strip.show()

