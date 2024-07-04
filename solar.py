#!python3
import paho.mqtt.client as mqtt
import json 
import time
import logging
import sys
import base64

broker="192.168.1.210"
port =1883
logging.basicConfig(level=logging.INFO)
#use DEBUG,INFO,WARNING

#check logging info 
def on_log(client, userdata, level, buf):
   logging.info(buf) 


#check connection status 
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        logging.info("connected OK")
    else:
        logging.info("Bad connection Returned code="+str(rc))
        client.loop_stop()  


#check disconnected status 
def on_disconnect(client, userdata, rc):
   logging.info("client disconnected ok")

#publishing data -> 
# def on_publish(client, userdata, mid):
#     logging.info("In on_pub callback mid= "  + str(mid))


def on_subscribe(client,userdata,mid,granted_qos):
    logging.info("in on subscribe callback result "+str(mid))
    for t in topic_ack:
        if t[1]==mid:
            t[2]=1 #set acknowledged flag
            logging.info("subscription acknowledged  "+t[0])
            client.suback_flag=True

#Message from the subscribed topic 
def on_message(client, userdata, message):
    topic=message.topic
    msgr=message.payload.decode()
    #print(base64.b64decode(msgr).decode('utf-8'))
    #msgr="Me(ssage Received topic="+topic+ " message ="+msgr
    print(msgr)
    print(type(msgr))
    logging.info(msgr)

#Subrscribing to the topic 
def check_subs():
    #returns false if have an unacknowledged subsription
    for t in topic_ack:
        if t[2]==0:
            logging.info("subscription to "+t[0] +" not acknowledged")
            return(False)
    return True 

#create flag in class
mqtt.Client.connected_flag=False

#create new instance 
client = mqtt.Client("python1")             
client.on_log=on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
# client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message
topics=[("solar/p01/metrics",0)]
data_out=json.dumps(topics)
topic_ack=[]
print("Connecting to broker ",broker)


####json data splitting 
print("*****************************")
data_out=json.dumps(topics)
data_topic = json.load(topics)
print(data_topic)
print("spliting to json", data_out)
print("*****************************")

try:
    client.connect(broker)      #connect to broker
except:
    print("can't connect")
    sys.exit(1)
client.loop_start()  #Start loop 
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
####


# Subcribing to the topics -> currently subcribed to only 2 topics    
# topics=[("house/lights/bulb1",0),("house/lights/bulb2",0)]  
print("subscribing  " + str(topics))
for t in topics:
    try:
        r=client.subscribe(t)
        if r[0]==0:
            logging.info("subscribed to topic "+str(t[0])+" return code" +str(r))
            #keep track of subscription
            topic_ack.append([t[0],r[1],0]) 
        else:
            logging.info("error on subscribing "+str(r))
            client.loop_stop()    #Stop loop 
            sys.exit(1)
    except Exception as e:
        logging.info("error on subscribe"+str(e))
        client.loop_stop()    #Stop loop 
        sys.exit(1)
print("waiting for all subs")
while not check_subs():
    time.sleep(1)
########


msg="off"
#print("Publishing topic= ",topics[0][0]," message= ",msg)
#client.publish(topics[0][0],msg)
time.sleep(4)
client.loop_stop()    #Stop loop 
client.disconnect() # disconnect



