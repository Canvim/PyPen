import time
import sys

from pypen.drawing.primitives import PrimitivesDrawer
from pyglet import clock, gl, image, window, canvas
import cairo


class PyPenWindow(window.Window):
    def __init__(self, user_sketch=None, window_title="Example", arguments={}):
        super().__init__(visible=False, resizable=True, caption=window_title, fullscreen=arguments.fullscreen)

        self.set_vsync(True)

        self.user_sketch = user_sketch
        self.window_title = window_title
        self.arguments = arguments
        self.passed_time = self.delta_time = self.frame_count = 0

        if not arguments.fullscreen:
            self.set_size(self.user_sketch.settings.width, self.user_sketch.settings.height)
        else:
            display = canvas.Display()
            screen = display.get_default_screen()
            self.user_sketch.settings.width = screen.width
            self.user_sketch.settings.height = screen.height

        self.primitives_drawer = PrimitivesDrawer(self.user_sketch.settings)
        self.fix_primitive_functions()

        clock.schedule_once(self.call_user_start, 0)
        if self.arguments.timeout:
            clock.schedule_once(self.destroy, self.arguments.timeout/1000)

    def on_mouse_motion(self, x, y, dx, dy):
        self.user_sketch.MOUSE.x = x
        self.user_sketch.MOUSE.y = self.user_sketch.settings.height - y

    def destroy(self, *args):
        self.close()

    def on_draw(self):
        gl.glEnable(gl.GL_TEXTURE_2D)

        gl.glBindTexture(gl.GL_TEXTURE_2D, self.primitives_drawer.texture.id)
        gl.glTexImage2D(
            gl.GL_TEXTURE_2D,
            0,
            gl.GL_RGBA,
            self.primitives_drawer.settings.width,
            self.primitives_drawer.settings.height,
            0,
            gl.GL_BGRA,
            gl.GL_UNSIGNED_BYTE,
            self.primitives_drawer.surface_data)

        gl.glBegin(gl.GL_QUADS)
        gl.glTexCoord2f(0.0, 1.0)
        gl.glVertex2i(0, 0)
        gl.glTexCoord2f(1.0, 1.0)
        gl.glVertex2i(self.primitives_drawer.settings.width, 0)
        gl.glTexCoord2f(1.0, 0.0)
        gl.glVertex2i(self.primitives_drawer.settings.width, self.primitives_drawer.settings.height)
        gl.glTexCoord2f(0.0, 0.0)
        gl.glVertex2i(0, self.primitives_drawer.settings.height)
        gl.glEnd()

    def on_resize(self, width, height):
        super().on_resize(width, height)

        if width <= 0 or height <= 0:
            return

        self.user_sketch.settings.width = max(width, 1)
        self.user_sketch.settings.height = max(height, 1)
        self.primitives_drawer.update_settings(self.user_sketch.settings)

    def fix_primitive_functions(self):
        self.user_sketch.fill_screen = self.primitives_drawer.fill_screen
        self.user_sketch.clear_screen = self.primitives_drawer.clear_screen
        self.user_sketch.clear = self.primitives_drawer.clear

        self.user_sketch.rectangle = self.primitives_drawer.rectangle
        self.user_sketch.circle = self.primitives_drawer.circle
        self.user_sketch.arc = self.primitives_drawer.arc

        self.user_sketch.rotate = self.primitives_drawer.rotate
        self.user_sketch.translate = self.primitives_drawer.translate
        self.user_sketch.scale = self.primitives_drawer.scale
        self.user_sketch.save = self.primitives_drawer.save
        self.user_sketch.restore = self.primitives_drawer.restore

    def call_user_start(self, dt):
        if self.user_sketch.settings._user_has_start:
            self.user_sketch.start()
            if not self.arguments.fullscreen:
                self.set_size(self.user_sketch.settings.width, self.user_sketch.settings.height)

        self.set_visible()

        clock.schedule_interval_soft(self.pypen_loop, 1/self.user_sketch.settings.fps)

    def call_user_update(self):
        self.user_sketch.TIME = self.user_sketch.T = self.passed_time
        self.user_sketch.FRAME = self.user_sketch.F = self.frame_count
        self.user_sketch.DELTA_TIME = self.user_sketch.DT = self.delta_time
        self.user_sketch.FPS = clock.get_fps()

        self.user_sketch.WIDTH = self.user_sketch.settings.width
        self.user_sketch.HEIGHT = self.user_sketch.settings.height

        if self.user_sketch.settings._user_has_update:
            try:
                self.user_sketch.update()
            except KeyboardInterrupt as exception:
                sys.exit(self.destroy())

    def pypen_loop(self, dt, *args):
        self.delta_time = dt
        self.passed_time += dt
        self.frame_count += 1

        clock.unschedule(self.pypen_loop)
        self.call_user_update()
        clock.schedule_interval_soft(self.pypen_loop, 1/self.user_sketch.settings.fps)
