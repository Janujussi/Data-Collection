import paho.mqtt.client as mqtt
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D12)

# Print the values to the serial port
#host = “mqtt.thingspeak.com"
host = "mqtt.thingspeak.com"
port = 1883
username = "DQMEFwQ7AjEjBDAlJzEJIDQ"     # Write your MQTT device username here
password = "XDSmIgzHWC1phz4MQaMkprdC"   # Write MQTT device password here
channelID = "1539221"         # Write channel ID to here
writeAPIkey = "7LXJZ6AZQKG9UHJH"     # Write write API Key to here
topicName = "channels/" + channelID + "/publish/" + writeAPIkey
client = mqtt.Client()
client.username_pw_set(username,password)
client.connect(host, port)
client.loop_start()

try:
    while True:
        # Read Temperature and Humidity Values
        temperature_c = dhtDevice.temperature
        temperature = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F, Humidity: {}% ".format(temperature, humidity))
        # Publish Sensor Values...
        client.publish(topicName, "&field1=" + str(temperature) + "&field2=" + str(humidity) + "&status=MQTTPUBLISH")
        time.sleep(60)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()