import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import json

#Connection to MQTT broker
broker = "broker.hivemq.com"
client = mqtt.Client("raspberrypiLabGroupXX")
print("Connecting to MQTT broker ", broker)
client.connect(host=broker, port=1883)
client.loop_start()

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    measurements = {}
    measurements = {"labGroup": "groupXX", "temperature": temp, "humidity": humidity}

    client.publish(topic="IIoT/your_group", payload=json.dumps(measurements))
    print("Measurements sent")
    time.sleep(10)

