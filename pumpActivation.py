import RPi.GPIO as GPIO
import time

# takes arguments of pump pin number and pump runningtime

def makeDrink(pump, timeSleep):
    GPIO.setmode(GPIO.BCM)
    pinList = [18, 17, 24, 27, 22, 23]

    #loop through pins and set mode and state to 'low'

    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    try:

      # loops through all pumps and activates them

      for i in range(len(pump)):
          GPIO.output((int(pump[i])), GPIO.LOW)

      # find the pump with the shortest runningtime and sleeeps for that ammount of time
      # and then removes it from the lists the program iterates through. This process will
      # be looped until the length of the list is 0. Every sleep value will be itself
      # minus past sleep values

      lastTime = 0
      while (len(timeSleep)>0):
          lowest = int(timeSleep[0])
          for i in range(len(timeSleep)):
              if (int(timeSleep[i])<lowest):
                  lowest = int(timeSleep[i])
          time.sleep(lowest-lastTime)
          lastTime = lowest
          GPIO.output(int(pump[timeSleep.index(str(lowest))]), GPIO.HIGH)
          pump.pop(timeSleep.index(str(lowest)))
          timeSleep.pop(timeSleep.index(str(lowest)))

    except KeyboardInterrupt:
        print("  Quit")
