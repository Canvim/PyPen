# Pyper
[![Build Status](https://travis-ci.org/Canvim/Pyper.svg?branch=master)](https://travis-ci.org/Canvim/Pyper) [![PyPI - Version](https://img.shields.io/pypi/v/pyperlib.svg?logo=python&color=lightblue&label=Version)](https://pypi.org/project/pyperlib/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/pyperlib?color=lightgreen&label=Downloads&logo=pypi)](https://pypi.org/project/pyperlib/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Canvim/Pyper?color=purple&label=Size&logo=github)](https://github.com/Canvim/Pyper/) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Canvim/Pyper/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Canvim/Pyper/?branch=master)

A blank paper for your creative adventures in Python!

## What is Pyper?
Pyper tries to be the end-all solution to creative coding in Python. It provides very easy-to-use functions for drawing primitives to the screen and getting user input.

## How do I install Pyper?
Easy! just do:
* ```pip install pyperlib```

Check out the package on [Pypi](https://pypi.org/project/pyperlib/)!

## How do I use Pyper?
Here is a bare-minimum example of a Pyper sketch:

```python
# example_001.py
from pyperlib import *

def start():
    settings.fps = 70

x = 0

def update():
    global x
    x += 1
    rectangle(x, 100, 30, 100, "red")
```

Run it by calling:
* ```pyper example_001.py```
* (or ```pyperlib example_001.py```)
* (or ```python -m pyperlib example_001.py```)

### More Examples!
We have a folder filled with Pyper examples. [Check it out!](https://github.com/Canvim/Pyper/tree/master/examples)

## How does Pyper work?
Pyper utilizes pygame in the background for event-management, draw-calls and window-management.

We felt like there was always a bunch of overhead needed to get a pygame to work, and it had some weird quirks which always made for a half-baked user experience.

Pyper is basically doing all that boring stuff in the background and exposes simple drawing functions for you to use and express your creativity with.

What are you waiting for?

Install it now with ```pip install pyperlib```