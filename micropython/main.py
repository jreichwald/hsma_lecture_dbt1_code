import ujson as json 

"""
A callback function which is called upon every arrival of subscribed mqtt messages
"""

def mqtt_cb(topic, msg):
    print(topic)
    print(msg)
    

mqttClient.set_callback(mqtt_cb)
mqttClient.connect()
mqttClient.subscribe("test")


while True:
    mqttClient.check_msg()  # Non-Blocking, use if e.g. when also publishing messages
    # mqttClient.wait_msg() # Blocking, use if controller only waits for messages to arrive (sleep not required then) 
    time.sleep(1)
    
    mqttClient.publish("myTopic", "MyMessage") 



