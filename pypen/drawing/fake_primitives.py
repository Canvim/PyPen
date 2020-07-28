

def clear_screen():
    """Clears the screen"""
    raise NotImplementedError("clear_screen() not implemented")


def clear():
    """Clears the screen"""
    raise NotImplementedError("clear() not implemented")


def fill_screen(color="default_background_color"):
    """Fills the screen with the specified color"""
    raise NotImplementedError("fill_screen() not implemented")


def fill():
    """Fills the current path"""
    raise NotImplementedError("fill() not implemented")


def rectangle(x, y, width, height, color="default_color"):
    """Draws a rectangle on the given coordinate with the given width, height and color"""
    raise NotImplementedError("rectangle() not implemented")


def circle(x, y, radius, color="default_color"):
    """Draws a circle on the given coordinate with the given radius and color"""
    raise NotImplementedError("circle() not implemented")


def ellipse(x, y, width, height, color="default_color"):
    """Draws an ellipse on the given coordinate with the given width, height and color"""
    raise NotImplementedError("ellipse() not implemented")


def arc(x, y, radius, start_angle, stop_angle, color="default_color"):
    """Draws an arc on the given coordinate with the given radius, angles and color"""
    raise NotImplementedError("arc() not implemented")


def rotate(angle):
    """Rotates the context"""
    raise NotImplementedError("rotate() is not implemented")


def translate(x, y):
    """Translates the context by x and y"""
    raise NotImplementedError("translate() is not implemented")


def scale(factor):
    """Scales the context by the provided factor"""
    raise NotImplementedError("scale() is not implemented")


def save():
    """Saves the current context's translation, rotation and scaling"""
    raise NotImplementedError("save() is not implemented")


def restore():
    """Restores the context's translation, rotation and scaling to that of the latest save"""
    raise NotImplementedError("restore() is not implemented")
