

class Settings:
    def __init__(self, fps, opengl_version):
        self.fps = fps
        self.opengl_version = opengl_version


settings = Settings(
    opengl_version=300,
    fps=60
)
