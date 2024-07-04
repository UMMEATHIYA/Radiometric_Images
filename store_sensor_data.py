import paho.mqtt.client as mqtt
import json 
import sqlite3
import time
import logging
import sys
import datetime 


DB_Name = "solar_panel_sep01.db"

# #database connection
# connection = sqlite3.connect("new_solar.db")
# cursor = connection.cursor() 

class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return
    
    def __del__(self):
        self.cur.close()
        self.conn.close()

###################################################

def mbox1_Handler(jsonData):
    #Parse Data 
    json_Dict = json.loads(jsonData)
    average = json_Dict['avg']
    minimum = json_Dict['min']
    maximum = json_Dict['max']
    maxpos_x = json_Dict['maxpos']['x']
    maxpos_y = json_Dict['maxpos']['y']
    minpos_x = json_Dict['minpos']['x']
    minpos_y = json_Dict['minpos']['y']
    unit = json_Dict['unit']
    # json_Dict['date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    # Date = json_Dict['date'] see even for ID i am not fetching values from the database it is autoincrement values.


    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into mbox1 (avg, min, max, maxpos_x, maxpos_y, minpos_x, minpos_y, unit) values (?,?,?,?,?,?,?,?)",[average, minimum, maximum, maxpos_x, maxpos_y, minpos_x, minpos_y, unit])
    del dbObj
    print("Inserted mbox1 Data into Database")
    print("")

# Function to save to DB Table
def mbox2_Handler(jsonData):
    #Parse Data 
    json_Dict = json.loads(jsonData)
    average = json_Dict['avg']
    minimum = json_Dict['min']
    maximum = json_Dict['max']
    maxpos_x = json_Dict['maxpos']['x']
    maxpos_y = json_Dict['maxpos']['y']
    minpos_x = json_Dict['minpos']['x']
    minpos_y = json_Dict['minpos']['y']
    unit = json_Dict['unit']
    # json_Dict['date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    # Date = json_Dict['date']

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into mbox2 (avg, min, max, maxpos_x, maxpos_y, minpos_x, minpos_y, unit) values (?,?,?,?,?,?,?,?)",[average, minimum, maximum, maxpos_x, maxpos_y, minpos_x, minpos_y, unit])
    del dbObj
    print("Inserted mbox2 Data into Database")
    print("")

def mbox3_Handler(jsonData):
    #Parse Data 
    json_Dict = json.loads(jsonData)
    average = json_Dict['avg']
    minimum = json_Dict['min']
    maximum = json_Dict['max']
    maxpos_x = json_Dict['maxpos']['x']
    maxpos_y = json_Dict['maxpos']['y']
    minpos_x = json_Dict['minpos']['x']
    minpos_y = json_Dict['minpos']['y']
    unit = json_Dict['unit']
    # json_Dict['date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    # Date = json_Dict['date']

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into mbox3 (avg, min, max, maxpos_x, maxpos_y, minpos_x, minpos_y, unit) values (?,?,?,?,?,?,?,?)",[average, minimum, maximum, maxpos_x, maxpos_y, minpos_x, minpos_y, unit])
    del dbObj
    print("Inserted mbox3 Data into Database")
    print("")

def mbox4_Handler(jsonData):
    #Parse Data 
    json_Dict = json.loads(jsonData)
    average = json_Dict['avg']
    minimum = json_Dict['min']
    maximum = json_Dict['max']
    maxpos_x = json_Dict['maxpos']['x']
    maxpos_y = json_Dict['maxpos']['y']
    minpos_x = json_Dict['minpos']['x']
    minpos_y = json_Dict['minpos']['y']
    unit = json_Dict['unit']
    # json_Dict['date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    # Date = json_Dict['date']

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into mbox4 (avg, min, max, maxpos_x, maxpos_y, minpos_x, minpos_y, unit) values (?,?,?,?,?,?,?,?)",[average, minimum, maximum, maxpos_x, maxpos_y, minpos_x, minpos_y, unit])
    del dbObj
    print("Inserted mbox4 Data into Database")
    print("")


#Solar Sensor data -> Bus Voltage, Shunt Voltage, current, line-voltage, p

def solar_sensor_Handler(jsonData):
    #Parse Data 
    received_data_payload = jsonData.decode()    
    received_data_payload = received_data_payload.replace("'",'"')
    
    json_Dict = json.loads(received_data_payload)
    print("sensor data",json_Dict)
    bus_voltage = json_Dict['bv']
    shunt_voltage = json_Dict['sv']
    current = json_Dict['i']
    line_voltage = json_Dict['lv']
    power = json_Dict['p']
    # json_Dict['date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    # Date = json_Dict['date']

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into solar_sensor (bv, sv, i, lv, p) values (?,?,?,?,?)",[bus_voltage,shunt_voltage, current, line_voltage, power])
    del dbObj
    print("Inserted solar_sensor Data into Database")
    print("")

# Master Function to Select DB Function based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
    if Topic == "FLIR/ec501-106AAB/mbox1":
        mbox1_Handler(jsonData)
    elif Topic == "FLIR/ec501-106AAB/mbox2":
        mbox2_Handler(jsonData)
    elif Topic == "FLIR/ec501-106AAB/mbox3":
        mbox3_Handler(jsonData)
    elif Topic == "FLIR/ec501-106AAB/mbox4":
        mbox4_Handler(jsonData)
    elif Topic == "solar/p01/metrics":
        solar_sensor_Handler(jsonData)
    
