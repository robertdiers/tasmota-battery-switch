# tasmota-battery-switch
Tasmota turns on/off power at a defined battery soc (Goodwe inverter)

### Defaults
plaese check properties in tasmota-battery-switch.ini file, could be overridden by Docker env variables

### Docker usage

environment variables:

MQTT_BROKER (default: 192.168.1.108)

MQTT_PORT (default: 1883)

MQTT_USER (default: admin)

MQTT_PASSWORD (default: password)

MQTT_NAMES (default: tasmota_nous_2,tasmota_nous_3,tasmota_nous_4)

BATTERY_ON (default: 100)

BATTERY_OFF (default: 40)

SEMS_USER (default: myid)

SEMS_PASSWORD (default: password)

SEMS_STATIONID (default: mystation)

docker run -d --restart always -e MQTT_BROKER=192.168.1.108 -e MQTT_PASSWORD=password --name tasmotabatteryswitch ghcr.io/robertdiers/tasmota-battery-switch:1.0

### create Docker image for your architecture
./image.sh


