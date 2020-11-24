# ESP32 Reference Setup 

## Intro and Prerequisites

This is the code for the ESP32 Reference Setup presened in the DBT1-Lecture. This code uses the following 
extra libraries (install them via Arduino IDE Library Manager): 

* [PubSubClient for connecting to MQTT](https://github.com/knolleary/pubsubclient)

Since no sensors need to be connected to run this simple mqtt-example, PubSubClient is the only lib needed.

## Setup 

You can just download the source code and open it with the Arduino-IDE. As long as the additional libraries are installed, it should compile out-of-the-box. You only need to set the following parameters (see comments in the source code): 

* Your WiFi Credentials 
* Your MQTT Broker credentials 
* The Topic(s) for Status messages and measured values
* The Client ID of your Device

