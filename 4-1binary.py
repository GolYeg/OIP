import RPi.GPIO as GPIO
import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    while(1):
        data = input()
        if data == 'q':
            break
        data = int(data)
        if data < 0 or data > 255:
            print("data<0")
            break
        GPIO.output(dac, decimal2binary(data))
        print("U = ",3.3*data/256)

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
    GPIO.cleanup()  

