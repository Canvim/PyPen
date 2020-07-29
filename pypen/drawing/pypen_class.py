import ctypes

from pypen.drawing.color import Color
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

        self.user_sketch.rectangle = self.rectangle
        self.user_sketch.circle = self.circle
        self.user_sketch.arc = self.arc

        self.user_sketch.rotate = self.rotate
        self.user_sketch.translate = self.translate
        self.user_sketch.scale = self.scale
        self.user_sketch.save = self.save
        self.user_sketch.restore = self.restore

    def _set_style(self, fill="", stroke="", stroke_width=-1):
        if fill != "":
            self.user_sketch.settings.fill = fill

        if stroke != "":
            self.user_sketch.settings.stroke = stroke

        if stroke_width >= 0:
            self.user_sketch.settings.stroke_width = stroke_width

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
        self.context.save()
        self.context.scale(self.user_sketch.settings.width, self.user_sketch.settings.height)
        self.rectangle(0, 0, 1, 1, color)
        self.context.restore()

    def fill(self):
        self.context.fill()

    def rectangle(self, x, y, width, height, color="default_color"):
        color = Color.from_user_input(color)

        self.context.set_source_rgba(*color.rgba())
        self.context.rectangle(x, y, width, height)
        self.context.fill()

    def circle(self, x, y, radius, color="default_color"):
        color = Color.from_user_input(color)

        self.context.set_source_rgba(*color.rgba())
        self.context.arc(x, y, radius, 0, 3.141593*2)
        self.context.fill()

    def ellipse(self, x, y, width, height, color="default_color"):
        color = Color.from_user_input(color)
        display = pygame.display.get_surface()

        rect_x = int(x - width/2)
        rect_y = int(y - height/2)
        pygame.draw.ellipse(display, color.rgba(), (rect_x, rect_y, int(width), int(height)))

    def arc(self, x, y, radius, start_angle, stop_angle, color="default_color"):
        color = Color.from_user_input(color)

        self.context.set_source_rgba(*color.rgba())
        self.context.set_line_width(1.4)
        self.context.arc(x, y, radius, start_angle, stop_angle)
        self.context.stroke()
