import time
import board
import busio
import digitalio
import adafruit_am2320
import datetime
import tweepy

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

#idovel kapcsolatos beallitasok
now=datetime.datetime.now()


# create the I2C shared bus
i2c = board.I2C()  # uses board.SCL and board.SDA
am = adafruit_am2320.AM2320(i2c)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

#Twitter beallitas
auth = tweepy.OAuthHandler('xWaOHMW9GSNgjsr8ShNu3LO1R','0TgRFHwvwouqziWclqtISPWajliqoR0RjAwyNJmyfQUtjXd5gg')
auth.set_access_token('1450813593969123330-r1sSJVNPCUujRXbdNa6kbrQR9Iz3qJ','POBpiQTXpVU2UWKXOPuRHsi8dpUgWQKaHgOnktBGAdNsM')

api = tweepy.API(auth)

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)



font = ImageFont.truetype('PixelOperator.ttf', 16)
#font = ImageFont.load_default()


i=0

while (i<100):

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    
    #ido frissitese
    now=datetime.datetime.now()

    #homerseklet es paratartalom bekerese
    TEMP=am.temperature
    HUM=am.relative_humidity

    # Pi Stats Display
    draw.text((0, 0), "Hömérséklet: " + str(TEMP) + " C°", font=font, fill=255)
    draw.text((0, 16), "Páratartalom: " + str(HUM) + "%", font=font, fill=255)
    draw.text((0, 32), "Utoljára mérve: ", font=font, fill=255)
    draw.text((39, 48), now.strftime("%H:%M:%S"), font=font, fill=255)

        
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(.1)
    i+=1
    if(i==100):
        oled.fill(0)
        oled.show()
        sztring = "Hőmérséklet: " + str(TEMP) + " C°, Páratartalom: " + str(HUM) + " %, Mérés ideje: " + str (now.strftime("%H:%M:%S"))
        api.update_status(sztring)
        print("Tweetelés->\n", sztring)
    
    




