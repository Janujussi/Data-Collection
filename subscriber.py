import paho.mqtt.client as Mqtt
from digitalOut import turnOn, turnOff, setMode		# Importing functions from digitalOut.py

# Sets GPIO pin 12 as output 
setMode()

# This is the MQTT Connection Settings
host = "mqtt.beebotte.com"
port = 1883
password = ""
username = "token_VRQVIkGlTNxnXcgl"
channel = "Lab_3"
resource = "sensor"
defStr = "Temperature"
topic = channel + "/" + resource

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(topic,1)

def on_message(client, userdata, msg):
	if defStr in str(msg.payload.decode()):
		print("Message Received:", str(msg.payload.decode()))
 	elif "ledON" in str(msg.payload.decode()):
		print("LED ON!")
		turnOn()
 	elif "ledOFF" in str(msg.payload.decode()):
		print("LED OFF!")
		turnOff()

client = Mqtt.Client() 
client.username_pw_set(username)
client.connect(host,port,60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()