import RPi.GPIO as GPIO
import time

RoAPin = 11
RoBPin = 12
RoSPin = 13

globalCounter = 0

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RoAPin, GPIO.IN)
    GPIO.setup(RoBPin, GPIO.IN)
    GPIO.setup(RoSPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    rotaryClear()

def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter
    Last_RoB_Status = GPIO.input(RoBPin)
    while(not GPIO.input(RoAPin)):   
        Current_RoB_Status = GPIO.input(RoBPin)
        flag = 1
    if flag == 1:
        flag = 0
        if(Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter = globalCounter + 1
            print("globalCounter = %d" % globalCounter)
        if(Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter = globalCounter - 1
            print("globalCounter = %d" % globalCounter)

def clear(ev=None):
    globalCounter = 0
    print("globalCounter = %d" % globalCounter)
    time.sleep(1)

def rotaryClear():
    GPIO.add_event_detect(RoSPin,GPIO.FALLING, callback=clear)
    # wait for falling

def loop():
    global globalCounter
    while True:
        rotaryDeal()
    

def destroy():
    GPIO.cleanup()

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
