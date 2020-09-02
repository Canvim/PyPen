
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


def reset_style():
    """Resets PyPen's current setting surrounding style to their default_values, which includes fill_color, stroke_color, stroke_width"""
    raise NotImplementedError("reset_style() is not implemented")


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


def begin_shape():
    """Tells PyPen that a shape is a bout to be created"""
    raise NotImplementedError("begin_shape() not implemented")


def vertex(x, y):
    """Adds a vertex to current shape at (x, y)"""
    raise NotImplementedError("vertex() not implemented")


def end_shape(fill_color="", stroke_color="", stroke_width=-1):
    """Ends shape and styles it"""
    raise NotImplementedError("end_shape() not implemented")


def rectangle(x, y, width, height, fill_color="", stroke_color="", stroke_width=-1):
    """Draws a rectangle on the given coordinate with the given width, height and color"""
    raise NotImplementedError("rectangle() not implemented")


def circle(x, y, radius, fill_color="", stroke_color="", stroke_width=-1):
    """Draws a circle on the given coordinate with the given radius and color"""
    raise NotImplementedError("circle() not implemented")


def ellipse(x, y, width, height, fill_color="", stroke_color="", stroke_width=-1):
    """Draws an ellipse on the given coordinate with the given width, height and color"""
    raise NotImplementedError("ellipse() not implemented")


def arc(x, y, radius, start_angle, stop_angle, fill_color="", stroke_color="", stroke_width=-1):
    """Draws an arc on the given coordinate with the given radius, angles and color"""
    raise NotImplementedError("arc() not implemented")

def triangle(x1, y1, x2, y2, x3, y3, fill_color="", stroke_color="", stroke_width=-1):
    """Draws a triangle between the supplied coordinates with the given color"""
    raise NotImplementedError("triangle() not implemented")

def line(x1, y1, x2, y2, stroke_color="", stroke_width=-1):
    """Draws a line between the supplied coordinates with the given stroke_color and stroke_width"""
    raise NotImplementedError("triangle() not implemented")
