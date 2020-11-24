#include <Arduino.h>
#include <Wire.h>
#include <WiFi.h>
#include <WiFiMulti.h>
#include <PubSubClient.h>

/* WiFi-Data */ 
const char *ssid = "YourWLANSSID";
const char *password = "YourWLANPassword";
WiFiMulti wifiMulti;

/* MQTT-Data */ 
const char *MQTTSERVER = "YourMQTTServerName"; 
const char *mqttuser = "YourMQTTUsername"; 
const char *mqttpasswd = "YourMQTTPassword"; 
const char *mqttdevice = "YourOwnClientName";  // Please use a unique name here!
WiFiClient wifiClient; 
PubSubClient client(wifiClient); 

/**
 * This function is called when a MQTT-Message arrives. 
 */
void mqtt_callback(char* topic, byte* payload, unsigned int length) {   //callback includes topic and payload ( from which (topic) the payload is comming)
  Serial.print("Message arrived ["); 
  Serial.print(topic); 
  Serial.print("]: ");
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println(""); 
 
}

/**
 * This function is called from setup() and establishes a MQTT connection.
 */ 
void initMqtt() {
  client.setServer(MQTTSERVER, 1883); 

  // Set the callback-Function when new messages are received.
  client.setCallback(mqtt_callback); 
  

  client.connect(mqttdevice, mqttuser, mqttpasswd); 
  while (!client.connected()) {
    Serial.print("."); 
    delay(500); 
  }

  // subscribe to a certain topic
  client.subscribe("myExampleTopicToSubscribeTo"); 
}

/**
 * This function is called from setup() and establishes a WLAN connection
 */ 

void initWifi() {
  Serial.println("Connecting to WiFi ..."); 
  wifiMulti.addAP(ssid, password);
  
  while (wifiMulti.run() != WL_CONNECTED) {
        Serial.print("."); 
        delay(500); 
    }

   Serial.println("");
   Serial.println("WiFi connected");
   Serial.println("IP address: ");
   Serial.println(WiFi.localIP());
}

/**
 * This function is called when the ESP is powered on. 
 */
void setup()
{
  // Set serial port speed to 115200 Baud 
  Serial.begin(115200);

  // Connect to WLAN 
  initWifi();  

  // Connect to MQTT server
  initMqtt(); 

  // Print to console 
  Serial.println("Setup completed.");
  delay(2000); 

}

/**
 * This function is the main function and loops forever. 
 */
void loop()
{
  // loop the mqtt client so it can maintain its connection and send and receive messages 
  client.loop(); 

  // wait a second before the next loop.
  delay(1000);   
}
