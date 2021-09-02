import paho.mqtt.client as mqtt
import json 

_username = "USERNAME"
_passwd = "PASSWORD"
_host = "HOST"
_port = 1883 
_timeout = 60 

lastValue = "INIT"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("dbt1/#")

def on_message(client, userdata, msg):
    if str(msg.topic) == "dbt1/demodata/sine": 
        processSineValue(json.loads(msg.payload.decode("utf-8")))
    elif str(msg.topic) == "dbt1/demodata/myactuator": 
        print(msg.payload)
    elif str(msg.topic) == "dbt1/jreichwald/dht11/values": 
        # processDht11Value(json.loads(msg.payload.decode("utf-8")))
        pass

def processSineValue(msg): 
    global lastValue

    if msg["sine_value"] < 0.0 and lastValue != "OFF":
        lastValue = "OFF"
        client.publish("dbt1/demodata/myactuator", lastValue)
    
    if msg["sine_value"] > 0.0 and lastValue != "ON":
        lastValue = "ON"
        client.publish("dbt1/demodata/myactuator", lastValue)
    
def processDht11Value(msg):
    print("something should be done with dh11-values ...")

client = mqtt.Client()
client.username_pw_set(_username, _passwd)
client.on_connect = on_connect
client.on_message = on_message

client.connect(_host, _port, _timeout)


client.loop_forever()