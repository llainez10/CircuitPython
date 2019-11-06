import time
import board

from fancyLED import FancyLED

D2 = board.D2
D3 = board.D3
D4 = board.D4
D5 = board.D5
D6 = board.D6
D7 = board.D7

fancy1 = FancyLED(D2, D3, D4)
fancy2 = FancyLED(D5, D6, D7)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()