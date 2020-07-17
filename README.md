# PyPen
[![Build Status](https://travis-ci.org/Canvim/PyPen.svg?branch=master)](https://travis-ci.org/Canvim/PyPen) [![PyPI - Version](https://img.shields.io/pypi/v/pypen.svg?logo=python&color=lightblue&label=Version)](https://pypi.org/project/pypen/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/pypen?color=lightgreen&label=Downloads&logo=pypi)](https://pypi.org/project/pypen/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Canvim/PyPen?color=purple&label=Size&logo=github)](https://github.com/Canvim/PyPen/) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Canvim/PyPen/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Canvim/PyPen/?branch=master)

Express your creativity through simple pens with PyPen!

## What is PyPen?
PyPen tries to be the end-all solution to creative coding in Python. It provides very easy-to-use functions for drawing primitives to the screen and getting user input.

## How do I install PyPen?
Easy! just do:
* ```pip install pypen```

Check out the package on [Pypi](https://pypi.org/project/pypen/)!

## How do I use PyPen?
Here is a bare-minimum example of a PyPen sketch:

```python
# example_001.py
from pypen import *

def start():
    settings.fps = 70

x = 0

def update():
    global x
    x += 1
    rectangle(x, 100, 30, 100, "red")
```

Run it by calling:
* ```pypen example_001.py```
* (or ```python -m pypen example_001.py```)

### More Examples!
We have a folder filled with PyPen examples. [Check it out!](https://github.com/Canvim/PyPen/tree/master/examples)

## How does PyPen work?
PyPen utilizes pygame in the background for event-management, draw-calls and window-management.

We felt like there was always a bunch of overhead needed to get a pygame to work, and it had some weird quirks which always made for a half-baked user experience.

PyPen is basically doing all that boring stuff in the background and exposes simple drawing functions for you to use and express your creativity with.

What are you waiting for?

Install it now with ```pip install pypen```