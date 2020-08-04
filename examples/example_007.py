from pypen import *


class Icon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.types = 2
        self.type = int(random(self.types))
        self.variation = random(1)
        self.width = 20
        self.color = "#383838"
        self.secondary_color = "#565656"

    def update(self):
        reset_style()
        save()
        translate(self.x, self.y)
        rotate(TIME)

        self.color = "#fe3060" if sqrt((self.x-MOUSE.x)**2 + (self.y-MOUSE.y)**2) <= 100 else "#383838"

        if self.variation > 0.5:
            rotate(90)

        if self.type == 0:
            self.rectangle()

        elif self.type == 1:
            self.circle()

        restore()

    def rectangle(self):
        if self.variation > 0.9:
            rectangle(0 - self.width/2, 0 - self.width/2, self.width, self.width, self.secondary_color)
            return

        rectangle(0 - self.width/2, 0 - self.width/2, self.width, self.width, self.color)

    def circle(self):
        circle(0, 0, self.width/2, self.color)
        if self.variation > 0.6:
            arc(0, 0, self.width/2, 0, PI, None, self.secondary_color, 2)


def start():
    settings.fps = 60

    global icons
    icons = []
    for x, y in grid(50):
        icons.append(Icon(x, y))


def update():
    fill_screen("#343434")

    for icon in icons:
        icon.update()

    circle(MOUSE.x, MOUSE.y, 100, (0, 0, 0, 100))
