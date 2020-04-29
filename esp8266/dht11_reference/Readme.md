# ESP8266 Reference Setup 

## Intro and Prerequisites

This is the code for the ESP8266 Reference Setup presened in the DBT1-Lecture. This code uses the following 
extra libraries (install them via Arduino IDE Library Manager): 

* [PubSubClient for connecting to MQTT](https://github.com/knolleary/pubsubclient)
* [ArduinoJSON for serializing JSON files](https://arduinojson.org/)
* [Arduino NTP Client for connecting to Internet Time Servers](https://github.com/arduino-libraries/NTPClient)
* [DHT Sensor Library for reading values out of the DHT11](https://github.com/adafruit/DHT-sensor-library)

## Wiring 
The Reference Setup is a NodeMCU ESP8266 Amica Board. The DHT11 should be wired as follows: 

* VCC pin of the DHT11 should be wired to the 3.3V power pin of the ESP (3V3)
* GND pin of the DHT11 should be wired to the GND pin of the ESP 
* Data pin of the DHT11 should be wired to D1 of the ESP

__Note:__ if you change the wiring of the data pin, you need to modify the code! 

## Setup 

You can just download the source code and open it with the Arduino-IDE. As long as the additional libraries are installed, 
it should compile out-of-the-box. You only need to set the following parameters (see comments in the source code): 

* Your WiFi Credentials 
* Your MQTT Broker credentials 
* The Topic(s) for Status messages and measured values
* The Client ID of your Device

