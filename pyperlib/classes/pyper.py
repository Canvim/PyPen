import moderngl
import moderngl_window as mglw


class Pyper(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (500, 400)
    title = "Pyper"  
    resizable = True
    samples = 8
    log_level = 0

    def __init__(self, **kwargs):  
        super().__init__(**kwargs)
