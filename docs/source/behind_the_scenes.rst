.. _behind the scenes:

How does PyPen *Really* Work?
-----------------------------

PyPen currently utilizes Pyglet in the background for event and window-management. For drawing, Cairo (through PyCairo) is used, making for a stable and quick svg drawing backend.

When you call ``pypen <your_sketch.py>`` PyPen 'imports' your sketch,
launces a Pyglet window, executes your start() function, and schedules
the update() function according to the specified framerate. It then
interprets and translates all your drawing functions and properly routes
Pyglet events to easy functions exposed to you and plants useful
variables such as ``DELTA_TIME``, ``WIDTH`` and more inside your sketch.

This means that all the PyPen user ever has to worry about is the fun
parts of creating a sketch, rather than all the boilerplate code usually involved (though some might disagree with the assessment of what is the fun part here xP).
