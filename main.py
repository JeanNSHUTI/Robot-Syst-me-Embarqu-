import RPi.GPIO as GPIO
from time import sleep


###     Setup     ###

GPIO.setmode(GPIO.BOARD)
PWMG = 7
MotorG_A = 12
MotorG_E = 22

PWMD = 18
MotorD_A = 16
MotorD_E = 15

#SensorRoueD = 15
#SensorRoueG = 11

#compteurG = 0
#compteurD = 0

#GPIO.setup(SensorRoueD,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(SensorRoueG,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(PWMG,GPIO.OUT)
G = GPIO.PWM(PWMG,100)

GPIO.setup(PWMD,GPIO.OUT)
D = GPIO.PWM(PWMD,100)

#GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(MotorG_A,GPIO.OUT)
GPIO.setup(MotorG_E,GPIO.OUT)

#GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(MotorD_A,GPIO.OUT)
GPIO.setup(MotorD_E,GPIO.OUT)

###     Interruption Capteur Roue Codeuse    ###
def IncrementSensorG(channel):
	global compteurG
        #print "compteurG = %d " %compteurG
	compteurG = compteurG + 1
        #GPIO.cleanup()

def IncrementSensorD(channel):
	global compteurD
	#print "compteurD = %d " %compteurD
	compteurD = compteurD + 1

#GPIO.add_event_detect(SensorRoueD, GPIO.RISING, callback = IncrementSensorG, bouncetime = 29)
#GPIO.add_event_detect(SensorRoueG, GPIO.RISING, callback = IncrementSensorD, bouncetime = 29)


###     Fonctions     ###

##   Avancer   ##
print "Forward"

#GPIO.output(Motor1A,GPIO.HIGH)
G.start(70)   #PWM
GPIO.output(MotorG_A,GPIO.LOW)
GPIO.output(MotorG_E,GPIO.HIGH)

#GPIO.output(Motor2A,GPIO.HIGH)
D.start(55) #PWM
GPIO.output(MotorD_A,GPIO.LOW)
GPIO.output(MotorD_E,GPIO.HIGH)

sleep(3)

#print "compteurD = %d " %compteurD
#print "compteurG = %d " %compteurG

print "Stopping motor"
#GPIO.output(Motor1E,GPIO.LOW)
#GPIO.output(Motor2E,GPIO.LOW)

GPIO.cleanup()





