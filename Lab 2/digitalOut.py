import RPi.GPIO as GPIO

# Sets pin 12 to output
def setMode():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12, GPIO.OUT)

# Sets pin 12 to HIGH
def turnOn():
	GPIO.output(12, GPIO.HIGH)

# Sets pin 12 to LOW
def turnOff():
	GPIO.output(12, GPIO.LOW)