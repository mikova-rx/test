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


GPIO.output(17, 1)
try:
    while True:
        print("Enter value > 25:")
        val = int(input())
        if val == -1:
            print("end")
            break
        lightnum(val)
        print(val,"=", val*0.0127)
finally:
    off()
