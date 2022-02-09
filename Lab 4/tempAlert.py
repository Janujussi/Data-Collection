import RPi.GPIO as GPIO
import urllib
import http.client
import requests
import time

# Pin definitions
led_pin = 23

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

interval = 10

# The sample method will take a single reading and return a
# compensated_reading object
try:
	while True:
		time.sleep(interval)
		response = requests.get("https://api.thingspeak.com/talkbacks/43975/commands.json?api_key=CO3T3T725V5EBZMR")
		data = response.json()
		print(data)

		if data != []:
			data = data[0] # Take the first element in data list which is a dictionary.

			if data.get("command_string") == "TURN_ON":
				print("LED is ON")
				GPIO.output(led_pin, 1)
				requests.delete("https://api.thingspeak.com/talkbacks/43975/commands.json?api_key=CO3T3T725V5EBZMR")

			elif data.get("command_string") == "TURN_OFF":
				print("LED is OFF")
				GPIO.output(led_pin, 0)
				requests.delete("https://api.thingspeak.com/talkbacks/43975/commands.json?api_key=CO3T3T725V5EBZMR")

except KeyboardInterrupt:
	print("connection failed!!")
	GPIO.cleanup()