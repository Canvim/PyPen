import ctypes

from pypen.drawing.color import Color
import cairo
from pyglet import gl, image

class PrimitivesDrawer():
    def __init__(self, settings):
        self.settings = settings
        self.surface_data = None
        self.surface = None
        self.context = None
        self.update_settings(settings)

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

    def update_settings(self, settings):
        self.settings = settings

        self.surface_data = (ctypes.c_ubyte * (self.settings.width * self.settings.height * 4))()
        self.surface = cairo.ImageSurface.create_for_data(
            self.surface_data,
            cairo.FORMAT_ARGB32,
            self.settings.width,
            self.settings.height,
            self.settings.width * 4)
        self.context = cairo.Context(self.surface)

        self.texture = image.Texture.create_for_size(gl.GL_TEXTURE_2D, self.settings.width, self.settings.height, gl.GL_RGBA)

    def clear_screen(self):
        self.fill_screen("default_background_color")

    def clear(self):
        self.clear_screen()

    def fill_screen(self, color="default_background_color"):
        self.context.save()
        self.context.scale(self.settings.width, self.settings.height)
        self.rectangle(0, 0, 1, 1, color)
        self.context.restore()

    def fill(self):
        pass

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
