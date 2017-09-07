import RPi.GPIO as GPIO
from time import sleep


###     Setup     ###

GPIO.setmode(GPIO.BOARD)
Motor1A = 16
Motor1B = 18
pinPWMG = 22

Motor2A = 19
Motor2B = 21
#Motor2E = 23
pinPWMD = 12

SensorRoueD = 15
SensorRoueG = 11

compteurG = 0
compteurD = 0


GPIO.setup(pinPWMD,GPIO.OUT)
D = GPIO.PWM(pinPWMD,100)

GPIO.setup(pinPWMG,GPIO.OUT)
G = GPIO.PWM(pinPWMG,100)

GPIO.setup(SensorRoueD,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SensorRoueG,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
#GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
#GPIO.setup(Motor2E,GPIO.OUT)

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

GPIO.add_event_detect(SensorRoueD, GPIO.RISING, callback = IncrementSensorG, bouncetime = 29)
GPIO.add_event_detect(SensorRoueG, GPIO.RISING, callback = IncrementSensorD, bouncetime = 29)


###     Fonctions     ###

##   Avancer   ##
print "Forward"

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
G.start(100)   #PWM
#GPIO.output(Motor1E,GPIO.HIGH)



GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
D.start(100) #PWM

#GPIO.output(Motor2E,GPIO.HIGH)

sleep(5)

print "compteurD = %d " %compteurD
print "compteurG = %d " %compteurG

print "Stopping motor"
#GPIO.output(Motor1E,GPIO.LOW)
#GPIO.output(Motor2E,GPIO.LOW)

GPIO.cleanup()






