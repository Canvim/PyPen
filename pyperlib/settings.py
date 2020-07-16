

class Settings:
    def __init__(self, fps, width, height, _is_executing_with_python, _user_has_start, _user_has_update, _has_already_saved_forced_screenshot):
        self.fps = fps
        self.width = width
        self.height = height

        self._is_executing_with_python = _is_executing_with_python
        self._user_has_start = _user_has_start
        self._user_has_update = _user_has_update
        self._has_already_saved_forced_screenshot = _has_already_saved_forced_screenshot


settings = Settings(
    width=640,
    height=480,
    fps=60,

    _is_executing_with_python=False,
    _user_has_start=True,
    _user_has_update=True,
    _has_already_saved_forced_screenshot=False
)
