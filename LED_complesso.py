import RPi.GPIO as GPIO
import time
import signal, os, sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def signal_handler(signum, frame):
    GPIO.output(18,GPIO.LOW)
    print("\nSet LED to LOW")
    sys.exit(0)

# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)

print ("Start blinking LED")
while True:
	GPIO.output(18,GPIO.HIGH)
	time.sleep(0.125)
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.125)


