from digitalio import DigitalInOut, Direction

class FancyLED:

    def __init__(self, alternate, blink, chase, sparkle):
        self.D2 = DigitalInOut.Output
        self.D3 = DigitalInOut.Output
        self.D4 = DigitalInOut.Output
        self.D5 = DigitalInOut.Output
        self.D6 = DigitalInOut.Output
        self.D7 = DigitalInOut.Output

    def alternate(self):
        self.D2.value = False
        self.D3.value = False
        self.D4.value = False
        self.D5.value = True
        self.D6.value = True
        self.D7.value = True

    def blink(self):
        self.D2.value = True
        self.D3.value = True
        self.D4.value = True
        self.D5.value = False
        self.D6.value = False
        self.D7.value = False


    def chase(self):
        self.D2.value = False
        self.D3.value = False
        self.D4.value = False
        self.D5.value = True
        self.D6.value = True
        self.D7.value = True

    def sparkle(self):
        self.D2.value = True
        self.D3.value = True
        self.D4.value = True
        self.D5.value = False
        self.D6.value = False
        self.D7.value = False