#!/usr/bin/env python

import datetime
import goodwe
import time

import Tasmota


class Goodwe:

    async def get_runtime_data(goodwe_ip, batteryon, batteryoff, mqtt_names):

        inverter = await goodwe.connect(goodwe_ip)
        runtime_data = await inverter.read_runtime_data()

        for sensor in inverter.sensors():
            if sensor.id_ in runtime_data:
                if 'battery_soc' in sensor.id_:
                    soc = float(runtime_data[sensor.id_])
                    if soc >= batteryon:
                        for name in mqtt_names.split(','):
                            print('ON ' + name)
                            Tasmota.on(name)
                            time.sleep(15)
                    if soc <= batteryoff:
                        for name in mqtt_names.split(','):
                            print('OFF ' + name)
                            Tasmota.off(name)
                            time.sleep(15)
                    # if soc >= 0:
                    #    for name in mqtt_names.split(','):
                    #        print('TEST ' + name)

                    print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " actualsoc: " + str(soc))
