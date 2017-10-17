import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
PWM = 18
GPIO.setup(PWM,GPIO.OUT)
D = GPIO.PWM(PWM,100)

D.start(50)

sleep(10)
GPIO.cleanup()
