import json 
import datetime 

devices = {}    # initialize empty dictionary 

devices["dht11"] = {"name" : "DHT11 Sensor", "timestamp" : datetime.datetime.now().isoformat(), "value" : 42}  # insert dht11 to dict
devices["dht22"] = {"name" : "DHT11 Sensor", "timestamp" : datetime.datetime.now().isoformat(), "value" : 38}  # insert dht22 to dict 

# show json output 
print(json.dumps(devices, indent=2)) 
