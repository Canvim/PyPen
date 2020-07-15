import pyglet


class PyperWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(200, 200)

    def exit_callback(self, dt):
        self.close()