import ctypes
import cairo

from pyglet import app, clock, gl, image, window

# create data shared by ImageSurface and Texture
width, height = 400, 400

surface_data = (ctypes.c_ubyte * (width * height * 4))()
surface = cairo.ImageSurface.create_for_data(surface_data, cairo.FORMAT_ARGB32, width, height, width * 4)
context = cairo.Context(surface)

texture = image.Texture.create_for_size(gl.GL_TEXTURE_2D, width, height, gl.GL_RGBA)

window = window.Window(width=width, height=height)

t = 0
def update(*args):
    global t
    t += 1
    context.save()
    context.scale(width, height)
    context.set_source_rgba(1.0, 1.0, 1.0, 1.0)
    context.rectangle(0, 0, 1, 1)
    context.fill()
    context.restore()

    context.set_source_rgba(0.5, 0.5, 0.0, 1.0)
    context.rectangle(t/10, 10, 100, 100)
    context.fill()


@window.event
def on_draw():

    # Draw texture backed by ImageSurface
    gl.glEnable(gl.GL_TEXTURE_2D)

    gl.glBindTexture(gl.GL_TEXTURE_2D, texture.id)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_BGRA, gl.GL_UNSIGNED_BYTE, surface_data)

    gl.glBegin(gl.GL_QUADS)
    gl.glTexCoord2f(0.0, 1.0)
    gl.glVertex2i(0, 0)
    gl.glTexCoord2f(1.0, 1.0)
    gl.glVertex2i(width, 0)
    gl.glTexCoord2f(1.0, 0.0)
    gl.glVertex2i(width, height)
    gl.glTexCoord2f(0.0, 0.0)
    gl.glVertex2i(0, height)
    gl.glEnd()


# call clock.schedule_update here to update the ImageSurface every frame
clock.schedule_interval(update, 1/60)
app.run()
