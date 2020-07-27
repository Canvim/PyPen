

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


def arc(x, y, width, height, start_angle, stop_angle, color="default_color"):
    """Draws an arc on the given coordinate with the given width, height, angled and color"""
    raise NotImplementedError("arc() not implemented")