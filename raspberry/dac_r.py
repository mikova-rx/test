import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
lednumbers = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(lednumbers, GPIO.OUT)


def off():
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    GPIO.output(13, 0)
    GPIO.output(6, 0)
    GPIO.output(5, 0)
    GPIO.output(11, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)



def dectobin(decnumber):
    arr = [0 for _ in range(8)]
    if decnumber == 0:
        return arr
    i = 0
    while decnumber != 1:
        arr[i] = decnumber%2
        decnumber = decnumber // 2
        i += 1
    arr[i] = (decnumber)
    arr.reverse()
    return arr
            


def lightnumber(value):
    declst = dectobin(value)
    for i in range(len(declst)):
        GPIO.output(lednumbers[i], declst[i])
    time.sleep(0.5)    



def num2dac(value):
    while True: 
        if value == -1:
            break
        lightnumber(value)


def repetitionnumber(rep):
    for i in range (rep):
        for j in range(0, 255):
            lightnumber(j)
            time.sleep(0.1)
        for j in range(255, 0, -1):
            lightnumber(j)
            time.sleep(0.1)

   
try:
    num2dac(9)
finally:
    off()    


 

