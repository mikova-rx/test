import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ledNumbers = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(ledNumbers, GPIO.OUT)


def lightUp(ledNumber, period):
        GPIO.output(ledNumber, 1)
        time.sleep(period)
        GPIO.output(ledNumber, 0)
        time.sleep(period)


#lightUp(21,1)


def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)
#blink(21, 3, 0.5)


def runningLight(count, period):
    for i in range(count):
        for ledNumber in ledNumbers:
            GPIO.output(ledNumber, 1)
            time.sleep(period)
            GPIO.output(ledNumber, 0)
            time.sleep(period)


def runningDark(count, period):
    for i in range(count):
        GPIO.output(ledNumbers, 1)
        for ledNumber in ledNumbers:
            GPIO.output(ledNumber, 0)
            time.sleep(period)
            GPIO.output(ledNumber, 1)
            time.sleep(period)
        GPIO.output(ledNumbers, 0)    
        
runningDark(1,0.5)

decNumber = int(input())


def decToBinList(decNumber):
    declist = [0 for _ in range(8)]
    if decNumber == 0:
        return declist
    j = 0
    while decNumber != 1:
        declist[j] = decNumber % 2
        decNumber = decNumber // 2
        j += 1
    declist[j] = (decNumber)
    declist.reverse()
    return declist

#print(decToBinList(decNumber))


number = int(input())


def lightNumber(number):
    declistt = decToBinList(number)
    for i in range(len(declistt)):
        GPIO.output(ledNumbers[i], declistt[i])
    time.sleep(1)


for i in ledNumbers:
    GPIO.output(i, 0)
lightNumber(number)






