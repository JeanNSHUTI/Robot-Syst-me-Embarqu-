import RPi.GPIO as GPIO
#from time import sleep
import time
import math
###     Fonctions     ###

###     Setup     ###
GPIO.setmode(GPIO.BOARD)

pulse_start = 0
pulse_end = 0

TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in


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
distance_mesuree_G = 0
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
	print "test1"
	while distance_mesuree_m < distance :
		ultrason()
		A1.start(80)   #PWM
		B1.start(0)
		A2.start(65) #PWM
		B2.start(0)
		distance_mesuree_m = (22*compteurD)/(20)	#Calculate average distance
	print "test2"
	compteurG = 0
	compteurD = 0
	distance_mesuree_m = 0
		
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
		distance_mesuree_m = (22*compteurD)/(20)	#Calculate average distance		
	compteurG = 0
	compteurD = 0
	distance_mesuree_m = 0
	
def turnLeft(rayon):
	print "turning left"
	global angle
	global distance_mesuree_m
	global compteurG
	distance_turn = rayon * math.pi * angle / 360
	GPIO.output(MotorD_E,GPIO.HIGH)
	GPIO.output(MotorG_E,GPIO.HIGH)
	
	while distance_mesuree_m < distance_turn:
		ultrason()
		A1.start(40)   #PWM
		B1.start(0)
		A2.start(65) #PWM
		B2.start(0)
		distance_mesuree_m = (22*compteurD)/(20)	#Calculate average distance
	distance_mesuree_m = 0
def turnRight(rayon):
	print "turning right"
	GPIO.output(MotorD_E,GPIO.HIGH)
	GPIO.output(MotorG_E,GPIO.HIGH)
	global angle
	global distance_mesuree_G
	global compteurG
	distance_turn = rayon * math.pi * angle / 360
	
	while distance_mesuree_G < distance_turn:
		ultrason()
		A1.start(80)   #PWM
		B1.start(0)
		A2.start(32.5) #PWM
		B2.start(0)
		distance_mesuree_G = (22*compteurG)/(20)	#Calculate average distance
	distance_mesuree_G = 0
	
def stop():
	print "Stopping motor"
	GPIO.output(MotorG_E,GPIO.LOW)
	GPIO.output(MotorD_E,GPIO.LOW)
	time.sleep(1)
	print "go"
	
def ultrason() :
	global pulse_start
	global pulse_end
	GPIO.output(TRIG, False)                 #Set TRIG as LOW
	print "Waitng For Sensor To Settle"
	time.sleep(0.001)                            #Delay of 2 seconds
  	GPIO.output(TRIG, True)                  #Set TRIG as HIGH

	time.sleep(0.00001)                      #Delay of 0.00001 seconds
  	GPIO.output(TRIG, False)                 #Set TRIG as LOw
  	
	while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    		pulse_start = time.time()              #Saves the last known time of LOW pulse

  	
	while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    		pulse_end = time.time()                #Saves the last known time of HIGH pulse 
  	
	pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
	print pulse_duration
  	distanceU = pulse_duration * 17150       #Multiply pulse duration by 17150 to get distance
  	distanceU = round(distanceU, 2)            #Round to two decimal points
  	if distanceU < 10:      #Check whether the distance is within range
    		print "Distance : ",distanceU," cm"  #Print distance with 0.5 cm calibration
		stop()


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
	if CurRotD == 20:
		RotationsD = RotationsD + 1
		CurRotD = 0
	
GPIO.add_event_detect(SensorRoueD, GPIO.RISING, callback = IncrementSensorG, bouncetime = 15)
GPIO.add_event_detect(SensorRoueG, GPIO.RISING, callback = IncrementSensorD, bouncetime = 15)
### Main ###


drive(100)
stop()
turnRight(30)#
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
