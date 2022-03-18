import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
try:
    
    p = GPIO.PWM(2, 1000)
    p.start(0)
    while(1):
        data = int(input())
        p.ChangeDutyCycle(data)


except ArithmeticError:
    print ("Arithmetic")
except ValueError:
    print ("ValueError")
except TypeError:
    print ("TypeError")        
finally:
    p.stop()
    GPIO.output(2, 0)

    GPIO.cleanup()
