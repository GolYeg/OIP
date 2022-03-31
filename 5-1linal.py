import RPi.GPIO as GPIO
import time

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for value in range (256):
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.005)
        compdata = GPIO.input(comp)
        if compdata == 0:
            return float(3.3*value/256)
            break


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)
try:
    GPIO.output(troyka, 1)
    while(1):
        vol = adc()
        print("input voltage = {:.2f}".format(vol))
        

except ArithmeticError:
    print ("Arithmetic")
except ValueError:
    print ("ValueError")
except TypeError:
    print ("TypeError")
except KeyboardInterrupt:
    print ("KeyboardInterrupt")
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()  

