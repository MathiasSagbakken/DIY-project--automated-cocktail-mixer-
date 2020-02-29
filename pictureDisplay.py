import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def currentDisplay(name):

    # pin configuration:

    RST = 12

    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

    disp.begin()

    # Clear display.

    disp.clear()
    disp.display()

    #adress of pciture file

    pictureAdress = '/home/pi/DrinkMixer/'+name

    # applies only pictures of a spesific size that fits the 1-inch oled screen

    if disp.height == 64:
        image = Image.open(pictureAdress).convert('1')
    else:
        image = Image.open(pictureAdress).convert('1')

    # Display image.
    disp.image(image)
    disp.display()
