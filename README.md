# PyPen
[![Build Status](https://travis-ci.org/Canvim/PyPen.svg?branch=master)](https://travis-ci.org/Canvim/PyPen) [![PyPI - Version](https://img.shields.io/pypi/v/pypen.svg?logo=python&color=lightblue&label=Version)](https://pypi.org/project/pypen/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/pypen?color=lightgreen&label=Downloads&logo=pypi)](https://pypi.org/project/pypen/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Canvim/PyPen?color=purple&label=Size&logo=github)](https://github.com/Canvim/PyPen/) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Canvim/PyPen/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Canvim/PyPen/?branch=master)

Express your creativity through simple pens with PyPen!

# What is PyPen?
PyPen tries to be the end-all solution to creative coding in Python. It provides very easy-to-use functions for drawing primitives to the screen and getting user input.

We felt like there was always a bunch of overhead needed to get nice and simple HTML-canvas-like graphics to work in Python and that it always made for a half-baked user experience.

PyPen is basically doing all of the boring stuff in the background and exposes simple functions like ```clear()```, ```circle(x, y, radius)```, ```rectangle(x, y, width, height)``` and many more for you to use and express your creativity with.

# How do I use PyPen?
### 1. Install PyPen
To install pypen, just do **```pip install pypen```**. To verify that it was installed correctly, run **```pypen --help```** (or ```python -m pypen --help```)

### 2. Create a PyPen Sketch
To create a basic sketch, just call **```pypen --init pypen_example.py```** (or whatever you want). This creates a file named 'pypen_example.py' (or whatever you provided the ```pypen --init``` with) which contains some PyPen code looking like this:

```python
from pypen import *


def start():
    settings.fps = 60


def update():
    fill("orange")
    rectangle(20, 20, 300, 400, "red")
```

(You of course don't have to use pypen --init to create all your sketches, but it's very convenient)

### 3. Run Your Sketch!
You can then run it by simply calling:
- **```pypen pypen_example.py```**
- (or ```python -m pypen pypen_example.py```)

### 4. Profit!
If everything worked, a window should launch containing something looking like this:

<img src="https://i.imgur.com/AwMJM3K.png" width="200px">

Wohoo! You made it! You have now launched your first PyPen sketch! Try changing some variables like the color from ```"red"``` to ```"blue"``` or the width and height of the rectangle (or maybe even change it into a circle!).

### 5. What now?
There is much more that PyPen can do that you have yet to discover. Interested in seeing how simple it is to use PyPen? We have an entire folder filled with interesting PyPen examples spanning from very simple to some more advanced ones as well. You find them in the 'examples/' folder on our repository located here:

### **[Examples!](https://github.com/Canvim/PyPen/tree/master/examples)**

---

## How does PyPen *really* work?
PyPen currently utilizes pygame in the background for event-management, draw-calls and window-management. In the future, we're considering making the switch to cairo (pycairo) to have a more robust, vector-based drawing-backend and perhaps a standard qtinker-window or maybe a pyglet one for event- and window-management. However, due to availability issues on windows with cairo and some failed attempts at drawing all primitives with OpenGL, we chose to use pygame in the meantime.

When you call ```pypen <your_sketch.py>``` PyPen 'imports' your sketch, launces a pygame window, executes your start() function, and schedules the update() function according to the specified framerate. It then interprets and translates all your drawing functions and properly routes pygame events to easy functions exposed to you and plants useful variables such as  ```DELTA_TIME```, ```WIDTH``` and more inside your sketch.

This means that all the PyPen user ever has to worry about is the fun parts (though some might disagree with that assessment xP) of creating a sketch.
