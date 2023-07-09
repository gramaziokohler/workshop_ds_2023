import board
import json
import pwmio
import socketpool
import ssl
import time
import wifi

from adafruit_motor import servo
from adafruit_minimqtt import adafruit_minimqtt as minimqtt


WIFI_SSID = "ttndemo"
WIFI_PASS = "transistor"

MQTT_HOST = "broker.hivemq.com"
MQTT_PORT = 1883
USERNAME = "enter-your-username"

pwm = pwmio.PWMOut(board.GP0, duty_cycle=2**13, frequency=50)
servo_motor = servo.Servo(pwm)

last_angle = 0.0


def map_value(target, range_from=(0, 135), range_to=(180, 0)):
    # maps target value in the range_from, to the range_to
    a, b = range_from
    c, d = range_to
    return c + ((d - c) / (b - a)) * (target - a)


class CubicEaseOut:
    limit = (0, 1)

    def __init__(self, start: float = 0, end: float = 1, duration: float = 1):
        self.start = start
        self.end = end
        self.duration = duration

    def ease(self, alpha: float) -> float:
        t = self.limit[0] * (1 - alpha) + self.limit[1] * alpha
        t /= self.duration
        a = self.func(t)
        return self.end * a + self.start * (1 - a)

    def func(self, t: float) -> float:
        return (t - 1) * (t - 1) * (t - 1) + 1


def servo_smooth_set(servo_motor, new_angle):
    global last_angle
    steps = 50
    fn = CubicEaseOut(start=last_angle, end=new_angle, duration=steps)

    for step in range(steps):
        angle = fn.ease(step)
        servo_motor.angle = int(angle)
        time.sleep(0.001)
    last_angle = new_angle


def set_servo_angle(servo_motor, angle):
    servo_smooth_set(servo_motor, int(map_value(angle)))
    # servo_motor.angle = int(map_value(angle))


print("Test servo")
set_servo_angle(servo_motor, 0)
time.sleep(2)
set_servo_angle(servo_motor, 135)
time.sleep(2)
set_servo_angle(servo_motor, 0)
time.sleep(2)
print("Done")


print(f"Connecting to Wi-Fi '{WIFI_SSID}'...")
wifi.radio.connect(WIFI_SSID, WIFI_PASS)
print(f"Connected! Your IP address is {wifi.radio.ipv4_address}")

pool = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()


def handle_connect(client, userdata, flags, rc):
    print(f"Connected to {client.broker}")
    mqtt_client.subscribe(f"/workshop_ds/values/" + USERNAME)


def handle_message(client, topic, message):
    data = json.loads(message)
    global servo_motor
    set_servo_angle(servo_motor, data["value"])
    print("New servo value on topic {0}: {1}".format(topic, data["value"]))


def handle_subscribe(mqtt_client, userdata, topic, granted_qos):
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


mqtt_client = minimqtt.MQTT(
    broker=MQTT_HOST,
    port=MQTT_PORT,
    socket_pool=pool,
    ssl_context=context,
)

mqtt_client.on_connect = handle_connect
mqtt_client.on_subscribe = handle_subscribe
mqtt_client.on_message = handle_message

print()
print(f"Connecting to {MQTT_HOST}...")
mqtt_client.connect()

while True:
    mqtt_client.loop()
    time.sleep(1)
