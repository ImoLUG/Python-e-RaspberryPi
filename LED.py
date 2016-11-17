import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

print ("Start blinking LED")
while True:
	GPIO.output(18,GPIO.HIGH)
	time.sleep(0.125)
	GPIO.output(18,GPIO.LOW)
	times.sleep(0.125)


