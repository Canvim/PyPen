from pypen.drawing.color import Color
import cairo


class PrimitivesDrawer():
    def __init__(self, surface, context, settings):
        self.surface = surface
        self.context = context
        self.settings = settings


    def update_settings(self, settings):
        self.settings = settings


    def clear_screen(self):
        self.fill_screen("default_background_color")


    def clear(self):
        self.clear_screen()


    def fill_screen(self, color="default_background_color"):
        self.rectangle(0, 0, self.settings.width, self.settings.height, color)


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
        self.context.arc(x, y, radius, 0, 3.141592*2)
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
