
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
Motor1A = 16
Motor1B = 18
Motor1E = 22

Motor2A = 19
Motor2B = 21
Motor2E = 23

SensorRoueD = 12
SensorRoueG = 11

compteurG = 0
compteurD = 0

#interruption
def IncrementSensorG(channel):
        print "compteurG = %d " %compteurG
        
		compteurG = compteurG + 1
        GPIO.cleanup()

def IncrementSensorD(channel):
		print "compteurD = %d " %compteurD
        print "droite"
		compteurD = compteurD + 1

GPIO.add_event_detect(SensorRoueD, GPIO.FALLING, callback = IncrementSensorG)
GPIO.add_event_detect(SensorRoueG, GPIO.FALLING, callback = IncrementSensorD)

GPIO.setup(SensorRoueD,GPIO.IN)
GPIO.setup(SensorRoueG,GPIO.IN)

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)




print "Forward"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(10)

print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)

GPIO.cleanup()






