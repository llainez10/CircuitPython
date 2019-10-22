# Write your code here :-)
import time
import board
import digitalio

photoint = digitalio.DigitalInOut(board.D7)
photoint.direction = digitalio.Direction.INPUT
photoint.pull = digitalio.Pull.UP

count = 0.0
lastTime = 0
lastState = True or False

while True:
    now = time.monotonic()
    if photoint.value:
        if lastState is True:
            count += 1
    if now > lastTime + 4:
        print("The Number of Interrupts is:")
        print(count)
        lastTime = now