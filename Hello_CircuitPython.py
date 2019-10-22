import board
import analogio
import time

led = analogio.AnalogOut(board.A0)
led.value = 0
led.value = 65535
led.value = 50000

10000 / 65535 * 3.3
0.5035477225909819
50000 / 65535 * 3.3
2.517738612954909

def dac_value(volts):
    return int(volts / 3.3 * 65535)

brightness = 3.3

while True:
    led.value = dac_value(brightness)
    time.sleep(0.1)
    brightness = round(brightness-0.05, 1)
    print(brightness)
    if brightness == 2.2:
        brightness = brightness+1.1