import time
import board
import busio
import digitalio
import adafruit_am2320


from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess


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

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)
#font = ImageFont.load_default()

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    TEMP=am.temperature
    HUM=am.relative_humidity

    # Pi Stats Display
    draw.text((0, 0), "Homerseklet: " + str(TEMP) + " C°", font=font, fill=255)
    draw.text((0, 16), "Paratartalom: " + str(HUM), font=font, fill=255)

        
    # Display image
    oled.image(image)
    oled.show()
    for i in range(14):
        time.sleep(0.5)
    oled.fill(0)
    oled.show()
    break


