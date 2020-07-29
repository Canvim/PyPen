import time
import sys
import os

from pypen.drawing.pypen_class import PyPen
from pyglet import clock, gl, image, window, canvas
import cairo


# In order to display our Icon properly on Windows,
# we need to have a "unique" (different from python's) app_id set
if sys.platform == "win32":
    import ctypes
    app_id = "canvim.pypen"  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)


class PyPenWindow(window.Window):
    def __init__(self, user_sketch=None, window_title="Example", arguments={}):
        super().__init__(visible=False, resizable=True, caption=window_title, fullscreen=arguments.fullscreen)

        self.set_vsync(True)
        self._current_path = os.path.dirname(__file__)
        self.set_icon(image.load(os.path.join(self._current_path, "..", "resources", "icon.png")))

        self.pypen = PyPen(user_sketch)
        self.window_title = window_title
        self.arguments = arguments
        self.passed_time = self.delta_time = self.frame_count = 0

        if not arguments.fullscreen:
            self.set_size(self.pypen.user_sketch.settings.width, self.pypen.user_sketch.settings.height)
        else:
            display = canvas.Display()
            screen = display.get_default_screen()
            self.pypen.user_sketch.settings.width = screen.width
            self.pypen.user_sketch.settings.height = screen.height

        clock.schedule_once(self.call_user_start, 0)
        if self.arguments.timeout:
            clock.schedule_once(self.destroy, self.arguments.timeout/1000)

    def on_mouse_motion(self, x, y, dx, dy):
        self.pypen.user_sketch.MOUSE.x = x
        self.pypen.user_sketch.MOUSE.y = self.pypen.user_sketch.settings.height - y

    def destroy(self, *args):
        self.close()

    def on_draw(self):
        gl.glEnable(gl.GL_TEXTURE_2D)

        gl.glBindTexture(gl.GL_TEXTURE_2D, self.pypen.texture.id)
        gl.glTexImage2D(gl.GL_TEXTURE_2D,
                        0,
                        gl.GL_RGBA,
                        self.pypen.user_sketch.settings.width,
                        self.pypen.user_sketch.settings.height,
                        0,
                        gl.GL_BGRA,
                        gl.GL_UNSIGNED_BYTE,
                        self.pypen.surface_data)

        gl.glBegin(gl.GL_QUADS)
        gl.glTexCoord2f(0.0, 1.0)
        gl.glVertex2i(0, 0)
        gl.glTexCoord2f(1.0, 1.0)
        gl.glVertex2i(self.pypen.user_sketch.settings.width, 0)
        gl.glTexCoord2f(1.0, 0.0)
        gl.glVertex2i(self.pypen.user_sketch.settings.width, self.pypen.user_sketch.settings.height)
        gl.glTexCoord2f(0.0, 0.0)
        gl.glVertex2i(0, self.pypen.user_sketch.settings.height)
        gl.glEnd()

    def on_resize(self, width, height):
        super().on_resize(width, height)

        if width <= 0 or height <= 0:
            return

        self.pypen.user_sketch.settings.width = max(width, 1)
        self.pypen.user_sketch.settings.height = max(height, 1)
        self.pypen.update_settings()

    def call_user_start(self, dt):
        if self.pypen.user_sketch.settings._user_has_start:
            self.pypen.user_sketch.start()
            if not self.arguments.fullscreen:
                self.set_size(self.pypen.user_sketch.settings.width, self.pypen.user_sketch.settings.height)

        self.set_visible()

        clock.schedule_interval_soft(self.pypen_loop, 1/self.pypen.user_sketch.settings.fps)

    def call_user_update(self):
        self.pypen.user_sketch.TIME = self.pypen.user_sketch.T = self.passed_time
        self.pypen.user_sketch.FRAME = self.pypen.user_sketch.F = self.frame_count
        self.pypen.user_sketch.DELTA_TIME = self.pypen.user_sketch.DT = self.delta_time
        self.pypen.user_sketch.FPS = clock.get_fps()

        self.pypen.user_sketch.WIDTH = self.pypen.user_sketch.settings.width
        self.pypen.user_sketch.HEIGHT = self.pypen.user_sketch.settings.height

        if self.pypen.user_sketch.settings._user_has_update:
            try:
                self.pypen.user_sketch.update()
            except KeyboardInterrupt as exception:
                sys.exit(self.destroy())

    def pypen_loop(self, dt, *args):
        self.delta_time = dt
        self.passed_time += dt
        self.frame_count += 1

        clock.unschedule(self.pypen_loop)
        self.call_user_update()
        clock.schedule_interval_soft(self.pypen_loop, 1/self.pypen.user_sketch.settings.fps)
