import board
import pwmio
import time

from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP0, duty_cycle=2**13, frequency=50)

servo_motor = servo.Servo(pwm)


def map_value(target, range_from=(0, 135), range_to=(180, 0)):
    # maps target value in the range_from, to the range_to
    a, b = range_from
    c, d = range_to
    return c + ((d - c) / (b - a)) * (target - a)


def set_servo_angle(servo_motor, angle):
    servo_motor.angle = int(map_value(angle))


print("Test servo motor")

while True:
    print("Move to 0")
    set_servo_angle(servo_motor, 0)
    time.sleep(2)

    print("Move to 45")
    set_servo_angle(servo_motor, 45)
    time.sleep(2)

    print("Move to 90")
    set_servo_angle(servo_motor, 90)
    time.sleep(2)

    print("Move to 135")
    set_servo_angle(servo_motor, 135)
    time.sleep(2)
