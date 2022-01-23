import time
import board
import busio
import digitalio
import adafruit_am2320
import datetime

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
    
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    temp = subprocess.check_output(cmd, shell = True )

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
    time.sleep(.3)




