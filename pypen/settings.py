from copy import copy

class Settings:
    def __init__(self, fps, width, height, default_pypen_name, _is_executing_with_python,
                 _user_has_start, _user_has_update, fill_color, stroke_color, stroke_width,
                 _shape_begun, _starting_point):
        self.fps = fps
        self.width = width
        self.height = height
        self.default_pypen_name = default_pypen_name
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width

        self._is_executing_with_python = _is_executing_with_python
        self._user_has_start = _user_has_start
        self._user_has_update = _user_has_update

        self._shape_begun = False
        self._starting_point = None


settings = Settings(width=640,
                    height=480,
                    fps=60,
                    default_pypen_name="my_sketch.py",
                    fill_color="default_fill_color",
                    stroke_color="default_stroke_color",
                    stroke_width=0,

                    _is_executing_with_python=False,
                    _user_has_start=True,
                    _user_has_update=True,

                    _shape_begun=False,
                    _starting_point=None)

default_settings = copy(settings)
