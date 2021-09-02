import json 
import datetime 
import numpy as np 

# Laden und parsen der JSON-Datei
# (normalerweise würden die Daten über das Netzwerk eintreffen, ist im Prinzip aber nichts anderes)
f = open('examplejson.json')
sensorreadings = json.load(f)

# Ausgabe aller Einträge des JSON-Files
for s in sensorreadings: 
    print(sensorreadings[s])

# Direkter Zugriff auf ein bestimmtes Feld: 
print("DHT11 aktueller Wert: " + str(sensorreadings["dht11"]["value"]))

# Berechnung des Durchschnitts der letzten Messungen des DHT22 
print("DHT22 Durchschnitt: " + str(np.mean(sensorreadings["dht22"]["lastMeasures"])))
