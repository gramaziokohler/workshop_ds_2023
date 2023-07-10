# This code runs on a Raspberry Pi Pico, it's almost python: it's called CircuitPython
# It will connect to the CO2 sensor plugged to the Pico, read the values and then publish them
# the sensor includes temperature and relative humidity

import board
import busio
import json
import socketpool
import ssl
import time
import wifi

import adafruit_scd4x
from adafruit_minimqtt import adafruit_minimqtt as minimqtt

# WiFi connection
WIFI_SSID = "ttndemo"
WIFI_PASS = "transistor"

print(f"Connecting to Wi-Fi '{WIFI_SSID}'...")
wifi.radio.connect(WIFI_SSID, WIFI_PASS)
print(f"Connected! Your IP address is {wifi.radio.ipv4_address}")

pool = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()

# MQTT connection
MQTT_HOST = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "gcasas"

mqtt = minimqtt.MQTT(
    broker=MQTT_HOST,
    port=MQTT_PORT,
    # client_id=MQTT_CLIENT_ID,
    socket_pool=pool,
    ssl_context=context,
)

print()
print(f"Connecting to {MQTT_HOST}...")
mqtt.connect()
print("Connected")

# Connect to sensor
i2c = busio.I2C(board.GP3, board.GP2)
scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()

# Read measurements and publish every 2 seconds
while True:
    if scd4x.data_ready:
        co2 = scd4x.CO2
        temperature = scd4x.temperature
        humidity = scd4x.relative_humidity

        mqtt.publish(
            f"/workshop_ds/sensors/co2/{MQTT_CLIENT_ID}", json.dumps(dict(value=co2))
        )
        mqtt.publish(
            f"/workshop_ds/sensors/temp/{MQTT_CLIENT_ID}",
            json.dumps(dict(value=temperature)),
        )
        mqtt.publish(
            f"/workshop_ds/sensors/humidity/{MQTT_CLIENT_ID}",
            json.dumps(dict(value=humidity)),
        )

        print(f"CO2: {co2} ppm")
        print(f"Temperature: {temperature:.1f} *C")
        print(f"Humidity: {humidity:.1f} %")
        print()

    mqtt.loop()
    time.sleep(2)
