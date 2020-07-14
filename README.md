# Pyper
[![Build Status](https://travis-ci.org/Canvim/Pyper.svg?branch=master)](https://travis-ci.org/Canvim/Pyper) [![PyPI - Version](https://img.shields.io/pypi/v/pyperlib.svg?logo=python&color=lightblue&label=Version)](https://pypi.org/project/pyperlib/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/pyperlib?color=lightgreen&label=Downloads&logo=pypi)](https://pypi.org/project/pyperlib/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Canvim/Pyper?color=purple&label=Size&logo=github)](https://github.com/Canvim/Pyper/)

A blank paper for your creative adventures in Python!

## What is Pyper?
Pyper tries to be the end-all solution to creative coding in Python. It provides very easy-to-use functions for drawing primitives to the screen and getting mouse input. It utilizes moderngl and pyglet in the background to efficiently utilize the GPU through OpenGL to draw everything quickly.

## How do I install Pyper?
Easy! just do:
* ```pip install pyperlib```

Thanks to moderngl, as long as you have a machine capable of running OpenGL 3.0+, everything will work fine, no matter if you use Linux, Windows or MacOs.

Check out the package on [Pypi](https://pypi.org/project/pyperlib/)!

## How do I use Pyper?
Here is a bare-minimum example of a Pyper sketch:

```python
# example_001.py
from pyperlib import *

def start():
    settings.fps = 120

x = 0

def update():
    x += 1
    rectangle(x, 100, 30, 100, colors.red)
```

Run by it calling:
* ```pyper example_001.py```
* (or ```pyperlib example_001.py```)
* (or ```python -m pyperlib ecample_001.py```)

### More Examples!
We have a folder filled with Pyper examples. [Check it out!](https://github.com/Canvim/Pyper/tree/master/examples)