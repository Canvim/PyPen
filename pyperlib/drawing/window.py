import time
from os import path, getcwd
from importlib import util as import_util

import pyglet
import moderngl

from pyperlib.settings import settings

context = moderngl.create_standalone_context()


class PyperWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(200, 200)

    def exit_callback(self, dt):
        self.close()


def run_pyper_window(arguments):
    file_path = path.join(getcwd(), arguments.filename)
    spec = import_util.spec_from_file_location("", file_path)
    user_sketch = import_util.module_from_spec(spec)
    spec.loader.exec_module(user_sketch)

    window = PyperWindow(
        resizable=True,
        fullscreen=arguments.fullscreen
    )

    context = moderngl.create_context(require=300)

    user_sketch.start()

    @window.event
    def on_draw():
        pass

    def update(delta_time):
        user_sketch.update()

    pyglet.clock.schedule_interval(update, 1/settings.fps)
    pyglet.clock.schedule_once(update, 0)

    if arguments.timeout > 0:
        pyglet.clock.schedule_once(window.exit_callback, arguments.timeout)
        pyglet.app.run()
    else:
        pyglet.app.run()
