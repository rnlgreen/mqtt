#!/usr/bin/python3
#Test script to send an MQTT message to Node-RED
import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("topic: {} received message = {}".format(str(message.topic),str(message.payload.decode("utf-8"))))

mqttBroker ="condor.rghome.local"

client = mqtt.Client("Test MQTT Client")
client.connect(mqttBroker) 

######Bind function to callback
client.on_message=on_message

#client.subscribe("temperature/+")
#client.subscribe("pressure/+")
client.subscribe("pico/#")

client.loop_start()

try:
    while True:
        time.sleep(0.1)

except:
    print ("Disconnecting")
    client.disconnect()
    client.loop_stop()

