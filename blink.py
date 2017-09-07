import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
while True:
	GPIO.output(5, False)
	time.sleep(1)
	GPIO.output(5, True)
	time.sleep(1)
