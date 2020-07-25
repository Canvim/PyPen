## [<- Back](https://github.com/Canvim/PyPen)

## How does PyPen *Really* Work?
PyPen currently utilizes pygame in the background for event-management, draw-calls and window-management. In the future, we're considering making the switch to cairo (pycairo) to have a more robust, vector-based drawing-backend and perhaps a standard qtinker-window or maybe a pyglet one for event- and window-management. However, due to availability issues on windows with cairo and some failed attempts at drawing all primitives with OpenGL, we chose to use pygame in the meantime.

When you call ```pypen <your_sketch.py>``` PyPen 'imports' your sketch, launces a pygame window, executes your start() function, and schedules the update() function according to the specified framerate. It then interprets and translates all your drawing functions and properly routes pygame events to easy functions exposed to you and plants useful variables such as  ```DELTA_TIME```, ```WIDTH``` and more inside your sketch.

This means that all the PyPen user ever has to worry about is the fun parts (though some might disagree with that assessment xP) of creating a sketch.