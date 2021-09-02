# ESP32 Reference Setup 

## Intro and Prerequisites

This is the code for the ESP32 Reference Setup presented in the DBT1-Lecture. This code uses the following 
extra libraries (install them via Arduino IDE Library Manager): 

* [PubSubClient for connecting to MQTT](https://github.com/knolleary/pubsubclient)
* [ArduinoJSON for creating and parsing JSON-Documents](https://arduinojson.org)
* [DHT11 Sensor Library](https://github.com/adafruit/DHT-sensor-library)

For this example, just the DHT11-Sensor is used.

## Setup 

You can just download the source code and open it with the Arduino-IDE. As long as the additional libraries are installed, it should compile out-of-the-box. You only need to set the following parameters (see comments in the source code): 

* Your WiFi Credentials 
* Your MQTT Broker credentials 
* The Topic(s) for Status messages and measured values
* The Client ID of your Device (__important!__ If you connect to the MQTT Broker using the same Client ID from different devices, existing connections will be closed and only the last established connection will remain active.)

