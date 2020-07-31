
def rotate(angle):
    """Rotates the context.

    Args:
        angle (float): The amount by which the context should be rotated.
    """
    raise NotImplementedError("rotate() is not implemented")


def translate(x, y):
    """Translates the context by x and y.

    Args:
        x (float): Horizontal coordinate.
        y (float): Vertical coordinate.
    """
    raise NotImplementedError("translate() is not implemented")


def scale(factor):
    """Scales the context by the provided factor

    Args:
        factor (float): The amount by which the current context should be scaled.
    """
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


def fill_screen(fill_color):
    """Fills the screen with the specified color

    Args:
        fill_color (Color): The color by which to fill the screen. Defaults to the theme's default background color.
    """
    raise NotImplementedError("fill_screen() not implemented")


def fill():
    """Fills the current path. Different from fill_screen."""
    raise NotImplementedError("fill() not implemented")


def rectangle(x, y, width, height, fill_color, stroke_color, stroke_width):
    """Draws a rectangle on the given coordinate with the given width, height and color

    Args:
        x (float): Horizontal coordinate.
        y (float): Vertical coordinate.
        width (float): Width of the triangle.
        height (float): Height of the triangle.
        fill_color (Color, optional): The color by which to fill the rectangle.
        stroke_color (Color, optional): The color of the rectangle's outline
        stroke_width (float, optional): The width of the outline.
    """
    raise NotImplementedError("rectangle() not implemented")


def circle(x, y, radius, fill_color, stroke_color, stroke_width):
    """Draws a circle on the given coordinate with the given radius and color

    Args:
        x (float): Horizontal coordinate.
        y (float): Vertical coordinate.
        radius (float): Radius of the circle.
        fill_color (Color, optional): The color by which to fill the circle.
        stroke_color (Color, optional): The color of the circle's outline
        stroke_width (float, optional): The width of the outline.
    """
    raise NotImplementedError("circle() not implemented")


def ellipse(x, y, width, height, fill_color="", stroke_color="", stroke_width=-1):
    """Draws an ellipse on the given coordinate with the given width, height and color

    Args:
        x (float): Horizontal coordinate.
        y (float): Vertical coordinate.
        width (float): Width of the ellipse.
        height (float): Height of the ellipse.
        fill_color (Color, optional): The color by which to fill the ellipse.
        stroke_color (Color, optional): The color of the ellipse's outline
        stroke_width (float, optional): The width of the outline.
    """
    raise NotImplementedError("ellipse() not implemented")


def arc(x, y, radius, start_angle, stop_angle, fill_color="", stroke_color="", stroke_width=-1):
    """Draws an arc on the given coordinate with the given radius, angles and color

    Args:
        x (float): Horizontal coordinate.
        y (float): Vertical coordinate.
        radius (float): Radius of the arc.
        start_angle (float): The angle from which to begin drawing the arc.
        stop_angle (float):  The angle at which to stop drawing the arc.
        fill_color (Color, optional): The color by which to fill the arc.
        stroke_color (Color, optional): The color of the arc's outline
        stroke_width (float, optional): The width of the outline.
    """
    raise NotImplementedError("arc() not implemented")
