

class Settings:
    def __init__(self, fps, width, height, default_pypen_name, _is_executing_with_python, _user_has_start, _user_has_update):
        self.fps = fps
        self.width = width
        self.height = height
        self.default_pypen_name = default_pypen_name

        self._is_executing_with_python = _is_executing_with_python
        self._user_has_start = _user_has_start
        self._user_has_update = _user_has_update


settings = Settings(width=640,
                    height=480,
                    fps=60,
                    default_pypen_name="my_sketch.py",

                    _is_executing_with_python=False,
                    _user_has_start=True,
                    _user_has_update=True)
