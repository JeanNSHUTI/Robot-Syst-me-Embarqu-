import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
PWM = 16

GPIO.setup(PWM,GPIO.OUT)
D = GPIO.PWM(PWM,100)

D.start(50)

GPIO.cleanup()
