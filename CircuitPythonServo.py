import time
import board
import pulseio
import touchio
from adafruit_motor import servo

touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A3 = touchio.TouchIn(board.A3)  # Not a touch pin on Trinket M0!
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
my_servo.angle = 0

while True:
    if touch_A1.value == 1:
        my_servo.angle = my_servo.angle+2
        time.sleep(0.1)
        print(my_servo.angle)

    if touch_A3.value == 1:
        my_servo.angle = my_servo.angle-2
        time.sleep(0.1)
        print(my_servo.angle)