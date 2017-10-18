import RPi.GPIO as GPIO
from time import sleep

###     Fonctions     ###

###     Setup     ###
GPIO.setmode(GPIO.BOARD)
PWMG = 7
MotorG_A = 12
MotorG_E = 22

PWMD = 18
MotorD_A = 16
MotorD_E = 15

GPIO.setup(PWMG,GPIO.OUT)
A1 = GPIO.PWM(PWMG,100)
GPIO.setup(MotorG_A,GPIO.OUT)
B1 = GPIO.PWM(MotorG_A,100)

GPIO.setup(PWMD,GPIO.OUT)
A2 = GPIO.PWM(PWMD,100)
GPIO.setup(MotorD_A,GPIO.OUT)
B2 = GPIO.PWM(MotorD_A,100)

def reverse():
	print "Reverse"
	#GPIO.output(Motor1A,GPIO.HIGH)

	A1.start(0)   #PWM
	B1.start(70)
	#GPIO.output(MotorG_A,GPIO.LOW)
	#GPIO.output(MotorG_E,GPIO.HIGH)
	
	A2.start(0) #PWM
	A2.start(60)
	#GPIO.output(MotorD_A,GPIO.LOW)
	
	GPIO.output(MotorD_E,GPIO.HIGH)
	GPIO.output(MotorG_E,GPIO.HIGH)
	
reverse()
sleep(2)

print "Stopping motor"
GPIO.output(MotorG_E,GPIO.LOW)
GPIO.output(MotorD_E,GPIO.LOW)