import time
import board
import adafruit_dht

# Initialize the DHT device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D12)

# Print the temperature and humidity values to the terminal
temperature = (dhtDevice.temperature) * (9 / 5) + 32
humidity = dhtDevice.humidity
print("Temp: {:.1f} F, Humidity: {}% ".format(temperature, humidity))