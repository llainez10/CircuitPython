import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    try:
        dist = sonar.distance
        if dist < 10:
            led.fill((255, 0, 0))
        else:
            led.fill((0, 255, 0))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
