import RPi.GPIO as GPIO
from time import sleep
import math
###     Fonctions     ###

###     Setup     ###
GPIO.setmode(GPIO.BOARD)


PWMG = 7
MotorG_A = 12
MotorG_E = 22

PWMD = 18
MotorD_A = 16
MotorD_E = 15

SensorRoueG = 13
SensorRoueD = 26

angle = 90
distance_mesuree_m = 0	
compteurG = 0		#Counts number of rising edges generated by wheel encoder over distance
compteurD = 0
CurRotG = 0			#Variable used to count rotations
CurRotD = 0
RotationsG = 0		#Holds number of rotations of wheels
RotationsD = 0

GPIO.setup(SensorRoueG,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SensorRoueD,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(PWMG,GPIO.OUT)    #Roue gauche
A1 = GPIO.PWM(PWMG,100)
GPIO.setup(MotorG_A,GPIO.OUT)
B1 = GPIO.PWM(MotorG_A,100)

GPIO.setup(PWMD,GPIO.OUT)   #Rou droite
A2 = GPIO.PWM(PWMD,100)
GPIO.setup(MotorD_A,GPIO.OUT)
B2 = GPIO.PWM(MotorD_A,100)

GPIO.setup(MotorG_E,GPIO.OUT)
GPIO.setup(MotorD_E,GPIO.OUT)


#Drives robot in forward drive
#Parameter : distance 	
def drive(distance):
	print "Forward"
	global distance_mesuree_m
	global compteurG
	global compteurD
	GPIO.output(MotorD_E,GPIO.HIGH)
	GPIO.output(MotorG_E,GPIO.HIGH)
	
	while distance_mesuree_m < distance :
	
		A1.start(80)   #PWM
		B1.start(0)
		A2.start(65) #PWM
		B2.start(0)
	
	compteurG = 0
	compteurD = 0
		
def reverse(distance):
	print "Reverse"
	global distance_mesuree_m
	global compteurG
	global compteurD
	GPIO.output(MotorD_E,GPIO.HIGH)
	GPIO.output(MotorG_E,GPIO.HIGH)
	
	while distance_mesuree_m < distance :
	
		A1.start(0)   #PWM
		B1.start(80)	
		A2.start(0) #PWM
		B2.start(65)	
		
	compteurG = 0
	compteurD = 0
	
def turnLeft(rayon):
	print "turning left"
	global angle
	global distance_mesuree_m
	distance_turn = rayon * math.pi * angle / 360
	while distance_turn < distance_mesuree_m:
		A1.start(0)   #PWM
		B1.start(40)
		A2.start(0) #PWM
		B2.start(65)

	
def turnRight(rayon):
	print "turning right"
	global angle
	global distance_mesuree_m
	distance_turn = rayon * math.pi * angle / 360
	while distance_turn < distance_mesuree_m:
		A1.start(80)   #PWM
		B1.start(0)
		A2.start(32.5) #PWM
		B2.start(0)

def stop():
	print "Stopping motor"
	GPIO.output(MotorG_E,GPIO.LOW)
	GPIO.output(MotorD_E,GPIO.LOW)



###     Interruptions for Capteur Roue Codeuse    ###
def IncrementSensorG(channel):
	global compteurG
	global CurRotG
	global RotationsG
	compteurG = compteurG + 1
	CurRotG = CurRotG + 1
	if CurRotG == 20:
		RotationsG = RotationsG + 1
		CurRotG = 0

def IncrementSensorD(channel):
	global compteurD
	global CurRotD
	global RotationsD
	compteurD = compteurD + 1
	CurRotD = CurRotD + 1
	distance_mesuree_m = (22*compteurD)/(20)	#Calculate average distance
	if CurRotD == 20:
		RotationsD = RotationsD + 1
		CurRotD = 0
	
GPIO.add_event_detect(SensorRoueD, GPIO.RISING, callback = IncrementSensorG, bouncetime = 15)
GPIO.add_event_detect(SensorRoueG, GPIO.RISING, callback = IncrementSensorD, bouncetime = 15)
### Main ###


drive(100)
stop()
turnRight(30)
stop()
drive(50)
stop()
turnLeft(30)
stop()
reverse(100)
#sleep(3.5)
#nombre_de_trous = compteurD 					#Average number of holes
print "compteurD = %d " %compteurD
print "compteurG = %d " %compteurG
print "\n{} Rotations!".format(RotationsD+1)
print "\n{} Rotations!".format(RotationsG+1)
print "Distance = %f " %distance_mesuree_m

stop()

GPIO.cleanup()
