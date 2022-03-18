import RPi.GPIO as GPIO
import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    period = int(input())
    for i in range(0, 256, 1):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(period/512)
        GPIO.output(dac, 0)
    for i in range(255, -1, -1):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(period/512)
        GPIO.output(dac, 0)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()  
