from digitalio import DigitalInOut, Direction

class RGB:

    def __init__(self, red, green, blue):
        self.r = DigitalInOut(red)
        self.r.direction = Direction.OUTPUT

        self.g = DigitalInOut(green)
        self.g.direction = Direction.OUTPUT

        self.b = DigitalInOut(blue)
        self.b.direction = Direction.OUTPUT

    def red(self):
        self.r.value = False
        self.g.value = True
        self.b.value = True

    def green(self):
        self.r.value = True
        self.g.value = False
        self.b.value = True

    def blue(self):
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def cyan(self):
        self.r.value = True
        self.g.value = False
        self.b.value = False

    def yellow(self):
        self.r.value = False
        self.g.value = False
        self.b.value = True

    def magenta(self):
        self.r.value = False
        self.g.value = True
        self.b.value = False



