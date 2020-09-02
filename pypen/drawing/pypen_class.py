import ctypes

from pypen.drawing.color import Color
from pypen.utils.math import TAU
from pypen.settings import default_settings
import cairo
from pyglet import gl, image

class PyPen():
    def __init__(self, user_sketch):
        self.user_sketch = user_sketch

        self.surface_data = None
        self.surface = None
        self.context = None

        self.update_settings()
        self._fix_primitive_functions()

    def _fix_primitive_functions(self):
        self.user_sketch.fill_screen = self.fill_screen
        self.user_sketch.clear_screen = self.clear_screen
        self.user_sketch.clear = self.clear

        self.user_sketch.begin_shape = self.begin_shape
        self.user_sketch.vertex = self.vertex
        self.user_sketch.end_shape = self.end_shape
        self.user_sketch.rectangle = self.rectangle
        self.user_sketch.circle = self.circle
        self.user_sketch.ellipse = self.ellipse
        self.user_sketch.arc = self.arc
        self.user_sketch.triangle = self.triangle
        self.user_sketch.line = self.line

        self.user_sketch.arc = self.arc

        self.user_sketch.rotate = self.rotate
        self.user_sketch.translate = self.translate
        self.user_sketch.scale = self.scale
        self.user_sketch.save = self.save
        self.user_sketch.restore = self.restore

        self.user_sketch.reset_style = self.reset_style

    def _fill(self, unparsed_fill_color):
        if unparsed_fill_color != "":
            self.user_sketch.settings.fill_color = unparsed_fill_color

        fill_color = Color.from_user_input(self.user_sketch.settings.fill_color)
        self.context.set_source_rgba(*fill_color.rgba())
        self.context.fill()

    def _stroke(self, unparsed_stroke_color, unparsed_stroke_width):
        if unparsed_stroke_color != "":
            self.user_sketch.settings.stroke_color = unparsed_stroke_color

        if unparsed_stroke_width >= 0:
            self.user_sketch.settings.stroke_width = unparsed_stroke_width

        stroke_color = Color.from_user_input(self.user_sketch.settings.stroke_color)
        stroke_width = self.user_sketch.settings.stroke_width

        self.context.set_line_width(stroke_width)
        self.context.set_source_rgba(*stroke_color.rgba())
        self.context.stroke_preserve()

    def rotate(self, angle=0):
        self.context.rotate(angle)

    def translate(self, x=0, y=0):
        self.context.translate(x, y)

    def scale(self, factor=1):
        self.context.scale(factor)

    def save(self):
        self.context.save()

    def restore(self):
        self.context.restore()

    def reset_style(self):
        self.user_sketch.settings.fill_color = default_settings.fill_color
        self.user_sketch.settings.stroke_color = default_settings.stroke_color
        self.user_sketch.settings.stroke_width = default_settings.stroke_width

    def update_settings(self):
        self.surface_data = (ctypes.c_ubyte * (self.user_sketch.settings.width * self.user_sketch.settings.height * 4))()
        self.surface = cairo.ImageSurface.create_for_data(self.surface_data,
                                                          cairo.FORMAT_ARGB32,
                                                          self.user_sketch.settings.width,
                                                          self.user_sketch.settings.height,
                                                          self.user_sketch.settings.width * 4)
        self.context = cairo.Context(self.surface)
        self.texture = image.Texture.create_for_size(gl.GL_TEXTURE_2D, self.user_sketch.settings.width, self.user_sketch.settings.height, gl.GL_RGBA)

    def clear_screen(self):
        self.fill_screen("default_background_color")

    def clear(self):
        self.clear_screen()

    def fill_screen(self, color="default_background_color"):
        background_color = Color.from_user_input(color)
        self.context.save()
        self.context.scale(self.user_sketch.settings.width, self.user_sketch.settings.height)
        self.context.rectangle(0, 0, 1, 1)
        self.context.set_source_rgba(*background_color.rgba())
        self.context.fill()
        self.context.restore()

    def begin_shape(self):
        self.user_sketch.settings._shape_begun = True

    def vertex(self, x, y):
        if self.user_sketch.settings._shape_begun:
            self.context.move_to(x, y)
            self.user_sketch.settings._starting_point = (x, y)
            self.user_sketch.settings._shape_begun = False
        else:
            self.context.line_to(x, y)

    def end_shape(self, fill_color="", stroke_color="", stroke_width=-1):
        if self.user_sketch.settings._starting_point is not None:
            starting_point = self.user_sketch.settings._starting_point
            self.context.line_to(starting_point[0], starting_point[1])
            self.user_sketch.settings._starting_point = None
        self._stroke(stroke_color, stroke_width)
        self._fill(fill_color)

    def rectangle(self, x, y, width, height, fill_color="", stroke_color="", stroke_width=-1):
        self.context.rectangle(x, y, width, height)
        self._stroke(stroke_color, stroke_width)
        self._fill(fill_color)

    def circle(self, x, y, radius, fill_color="", stroke_color="", stroke_width=-1):
        self.context.arc(x, y, radius, 0, TAU)
        self._stroke(stroke_color, stroke_width)
        self._fill(fill_color)

    def ellipse(self, x, y, width, height, fill_color="", stroke_color="", stroke_width=-1):
        ratio = height/width
        self.save()
        self.context.scale(1, ratio)
        self.context.arc(x, y/ratio, width, 0, TAU)
        self.restore()
        self._stroke(stroke_color, stroke_width)
        self._fill(fill_color)

    def arc(self, x, y, radius, start_angle, stop_angle, fill_color="", stroke_color="", stroke_width=-1):
        self.context.arc(x, y, radius, start_angle, stop_angle)
        self._stroke(stroke_color, stroke_width)
        self._fill(fill_color)

    def triangle(self, x1_or_x, y1_or_y, x2_or_width, y2_or_height, x3_or_p=0.5, y3=None, fill_color="", stroke_color="", stroke_width=-1):
        if y3 is not None:
            x1 = x1_or_x
            y1 = y1_or_y
            x2 = x2_or_width
            y2 = y2_or_height
            x3 = x3_or_p
        else:
            x = x1_or_x
            y = y1_or_y
            width = x2_or_width
            height = y2_or_height
            p = x3_or_p

            x1 = x - width/2
            y1 = y + height/2
            x2 = x + width/2
            y2 = x + height/2
            x3 = (x2 - x1) * p + x1
            y3 = y - height/2

        self.context.move_to(x1, y1)
        self.context.line_to(x2, y2)
        self.context.line_to(x3, y3)
        self.context.line_to(x1, y1)
        self._stroke(stroke_color, stroke_width)
        self._fill(fill_color)

    def line(self, x1, y1, x2, y2, stroke_color="", stroke_width=-1):
        self.context.move_to(x1, y1)
        self.context.line_to(x2, y2)
        self._stroke(stroke_color, stroke_width)
