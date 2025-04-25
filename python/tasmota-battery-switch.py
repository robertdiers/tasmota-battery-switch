#!/usr/bin/env python

import asyncio

import Goodwe_Local
import Tasmota
import Config

if __name__ == "__main__":  
    # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " START #####")
    try:
        conf = Config.read()
        batteryon = int(conf["battery_on"])
        batteryoff = int(conf["battery_off"])

        # connect interfaces
        Tasmota.connect(conf["mqtt_broker"], conf["mqtt_port"], conf["mqtt_user"], conf["mqtt_password"])

        # read Goodwe
        asyncio.run(Goodwe_Local.Goodwe.get_runtime_data(conf["goodwe_ip"], batteryon, batteryoff, conf["mqtt_names"]))

        # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " END #####")

    except Exception as ex:
        print("ERROR: ", ex)
