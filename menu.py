import gpiozero
import time
import RPi.GPIO as GPIO
import time
import threading
from sudoLed import ledOn
from pictureDisplay import currentDisplay
from pumpActivation import makeDrink

# Shows picture puzzle on boot
currentDisplay('puzzle.png')

# chooses the BCM preset for pins

GPIO.setmode(GPIO.BCM)

# button configurations

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# splits the values and make a list

def pumpConfig(str):
    splittedNways = str.split(",")
    return splittedNways

# picture/pump pins/pump runningtime

drinks = ["clean.jpg-18,17,24,27,22,23/20,20,20,20,20,20", "mm.png-18,17,23/30,40,40", "sd.jpg-18,24/30,60",
          "sotb.png-18,24,27,22/24,24,24,12", "ww.png-182722/40,60,20"]

def chooseDrink():

    # teller is responsible for rotating between options of drinks and will
    # for each number represent a possible drink

    teller=1

    # the program is to appear seamless so it will run on boot and
    # can not be shut down unless when the hardware also is turned off

    while True:
        pumpData = drinks[teller].split("-")
        pumpTime = pumpConfig(pumpData[1].split("/")[1])
        pumpNr = pumpConfig(pumpData[1].split("/")[0])

        # when button conncted to pin 19 is pressed it will choose the next
        # drink in the drink list  and display the image for that drink in the menu

        input_state3 = GPIO.input(19)
        if input_state3 == False:
            teller=teller+1
            if teller > len(drinks)-1:
                teller = 0
            data = drinks[teller].split("-")
            currentDisplay(data[0])

            # time.sleep is used so the button will only give 1 input every 0.2
            # seconds as opposed to thousands

            time.sleep(0.2)

        # when button conncted to pin 13 is pressed it will make the drink for
        # the current index teller has in the drink menu

        input_state2 = GPIO.input(13)
        if input_state2 == False:
            makeDrink(pumpNr, pumpTime)

            time.sleep(0.2)

        # when button conncted to pin 26 is pressed it will choose the previous
        # drink in the drink list and display the image for that drink in the menu

        input_state = GPIO.input(26)
        if input_state == False:
            teller=teller-1
            if teller < 0:
                teller = len(drinks)-1
            data = drinks[teller].split("-")
            currentDisplay(data[0])

            time.sleep(0.2)

chooseDrink()
gpio.cleanup()
