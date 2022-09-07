import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import json

#Callbacks functions for MQTT
def on_log(client, userdata, level, buf):
    print("log: "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection achieved")
    else:
        print("Wrong connection. Returned code=", rc)
def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected. Result code "+str(rc))


#Connection to MQTT broker
broker = "broker.hivemq.com"
client = mqtt.Client("raspberrypiLabGroupXX")
client.on_connect = on_connect 
client.on_disconnect = on_disconnect
client.on_log = on_log 

print("Connecting to MQTT broker ", broker)
client.connect(host=broker, port=1883)
client.loop_start()

sense = SenseHat 

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    measurements = {}
    measurements = {"labGroup": "groupXX", "temperature": temp, "humidity": humidity}

    client.publish(topic="IIoT/your_group", payload=json.dumps(measurements))
    print("Measurements sent")
    time.sleep(10)

