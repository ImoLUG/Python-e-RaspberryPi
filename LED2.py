import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

while True:
    GPIO.output(18,GPIO.HIGH)
    sys.stdin.read(1)
    GPIO.output(18,GPIO.LOW)
    sys.stdin.read(1)
