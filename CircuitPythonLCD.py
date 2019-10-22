import time
import board
import digitalio

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

button_a = digitalio.DigitalInOut(board.D7)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

button_b = digitalio.DigitalInOut(board.D2)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.UP

count = 0

while True:
    if not button_a.value:
        if button_b.value:
            count += 1
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("ButtonState:UP")
        else:
            count -= 1
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("ButtonState:DOWN")
        lcd.set_cursor_pos(1, 0)
        lcd.print("Presses:")
        lcd.set_cursor_pos(1, 8)
        lcd.print(str(count))
        time.sleep(0.0)
