#!/usr/bin/env python

import configparser
import os
from datetime import datetime

#read config
config = configparser.ConfigParser()

def read():
    try:
        #read config
        config.read('tasmota-battery-switch.ini')

        values = {}

        #read config and default values
        values["mqtt_broker"] = config['MqttSection']['mqtt_broker']
        values["mqtt_port"] = int(config['MqttSection']['mqtt_port'])
        values["mqtt_user"] = config['MqttSection']['mqtt_user']
        values["mqtt_password"] = config['MqttSection']['mqtt_password']
        values["mqtt_names"] = config['MqttSection']['mqtt_names']
        if os.getenv('MQTT_BROKER','None') != 'None':
            values["mqtt_broker"] = os.getenv('MQTT_BROKER')
            #print ("using env: MQTT_BROKER")
        if os.getenv('MQTT_PORT','None') != 'None':
            values["mqtt_port"] = int(os.getenv('MQTT_PORT'))
            #print ("using env: MQTT_PORT")
        if os.getenv('MQTT_USER','None') != 'None':
            values["mqtt_user"] = os.getenv('MQTT_USER')
            #print ("using env: MQTT_USER")
        if os.getenv('MQTT_PASSWORD','None') != 'None':
            values["mqtt_password"] = os.getenv('MQTT_PASSWORD')
            #print ("using env: MQTT_PASSWORD")
        if os.getenv('MQTT_NAMES','None') != 'None':
            values["mqtt_names"] = os.getenv('MQTT_NAMES')
            #print ("using env: MQTT_NAMES")
        
        values["battery_on"] = config['BatterySection']['battery_on']
        values["battery_off"] = int(config['BatterySection']['battery_off'])
        if os.getenv('BATTERY_ON','None') != 'None':
            values["battery_on"] = os.getenv('BATTERY_ON')
            #print ("using env: BATTERY_ON")
        if os.getenv('BATTERY_OFF','None') != 'None':
            values["battery_off"] = int(os.getenv('BATTERY_OFF'))
            #print ("using env: BATTERY_OFF")
        
        values["sems_user"] = config['GoodweSection']['sems_user']
        values["sems_password"] = config['GoodweSection']['sems_password']
        values["sems_stationid"] = config['GoodweSection']['sems_stationid']
        if os.getenv('SEMS_USER','None') != 'None':
            values["sems_user"] = os.getenv('SEMS_USER')
            #print ("using env: SEMS_USER")
        if os.getenv('SEMS_PASSWORD','None') != 'None':
            values["sems_password"] = os.getenv('SEMS_PASSWORD')
            #print ("using env: SEMS_PASSWORD")
        if os.getenv('SEMS_STATIONID','None') != 'None':
            values["sems_stationid"] = os.getenv('SEMS_STATIONID')
            #print ("using env: SEMS_STATIONID")
        
        #print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " config: ", values)

        return values
    except Exception as ex:
        print ("ERROR Config: ", ex) 
