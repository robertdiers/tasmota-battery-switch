#!/usr/bin/env python

from datetime import datetime

import Goodwe
import Tasmota
import Config

if __name__ == "__main__":  
    #print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " START #####")
    try:
        conf = Config.read()
        batteryon = int(conf["battery_on"])
        batteryoff = int(conf["battery_off"])
        
        #connect interfaces
        Tasmota.connect(conf["mqtt_broker"], conf["mqtt_port"], conf["mqtt_user"], conf["mqtt_password"])

        #read Goodwe
        res = Goodwe.read(conf["sems_user"], conf["sems_password"], conf["sems_stationid"])
        soc = int(res["soc"].strip('%'))
        
        if soc >= batteryon:
            for name in conf["mqtt_names"].split(','):
                print('ON ' + name)
                Tasmota.on(name)
        if soc <= batteryoff:
            for name in conf["mqtt_names"].split(','):
                print('OFF ' + name)
                Tasmota.off(name)
        #if soc >= 0:
        #    for name in conf["mqtt_names"].split(','):
        #        print('TEST ' + name)

        print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " actualsoc: " + res["soc"])

        #print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " END #####")
        
    except Exception as ex:
        print ("ERROR: ", ex) 
