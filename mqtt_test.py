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

client = mqtt.Client("Test MQTT Client 2")
client.connect(mqttBroker) 

######Bind function to callback
client.on_message=on_message

client.loop_start()
randNumber = uniform(20.0, 25.0)
client.subscribe("temperature/+")
client.publish("temperature/cupboard", randNumber)
randNumber = uniform(40.0, 75.0)
client.publish("temperature/cpu", randNumber)
time.sleep(3)

client.disconnect()
client.loop_stop()

