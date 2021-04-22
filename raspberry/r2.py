import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
lednums = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(lednums, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setwarnings(False)

def off():
    GPIO.output(lednums, 0)

def dtob(dnum):
    binarr = [0 for _ in range(8)]
    if dnum == 0:
        return binarr
    i = 0
    while dnum != 1:
        binarr[i] = dnum % 2
        dnum = dnum // 2
        i += 1
    binarr[i] = (dnum)
    #binarr.reverse()
    return binarr
        
def lightnum(val):
    decarr = dtob(val)
    for i in range(len(decarr)):
        GPIO.output(lednums[i], decarr[i])

def num2dac(val):
    n = [0, 0, 0, 0, 0, 0, 0, 0]   
    a = int(val / 256)
    b = val % 256   
    c = a + b
    n = lightnum(c)

def change_v():
    for digval in range (256):
        anval = digval*0.0127
        num2dac(digval)
        time.sleep(0.001)
        if GPIO.input(4) == 0:
            print("Digital value:",digval,",","Analog value:", anval, "V")
            break
    return digval

GPIO.output(17, 1)

while True:
    change_v()