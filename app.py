import paho.mqtt.client as mqtt
from store_sensor_data import sensor_Data_Handler

# MQTT Settings 
MQTT_Broker = "192.168.1.210"
MQTT_Port = 1883
Keep_Alive_Interval = 65535    #0 to 65535
MQTT_Topic = ["FLIR/ec501-106AAB/+", "solar/+/metrics"]

#current topics - [(["FLIR/ec501-106AAB/mbox1", 0], ["FLIR/ec501-106AAB/mbox2",0], ["FLIR/ec502-106AAB/mbox3",0], ["FLIR/ec502-106AAB/mbox4", 0])]

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, flags, rc):
	for mqtt_topic in MQTT_Topic:
		mqttc.subscribe(mqtt_topic)

# Save Data into DB Table
def on_message(mosq, obj, msg):
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print("MQTT Data Received...")
	print("MQTT Topic: " + msg.topic)  
	print("Data: " + str(msg.payload))
    #str(message.payload.decode("utf-8"))
	sensor_Data_Handler(msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()