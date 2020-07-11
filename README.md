# Pyper
![PyPI - Version](https://img.shields.io/pypi/v/pyperlib.svg?logo=python&color=lightblue&label=Pyper%20Version) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pyperlib?color=lightgreen&label=Pyper%20Downloads&logo=pypi) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Canvim/Pyper?color=purple&label=Pyper%20Size&logo=github) ![GitHub stars](https://img.shields.io/github/stars/Canvim/Pyper?color=gold&logo=github)

A blank paper for your creative adventures in Python!

## What is Pyper?
Pyper tries to be the end-all solution to creative coding in Python. It provides very easy-to-use functions for drawing primitives to the screen and getting mouse input. It utilizes moderngl and moderngl-window in the background to efficiently utilize the GPU through OpenGL to draw all primitives quickly.

## How do I install Pyper?
Easy! just do:
* ```pip install pyperlib```

Thanks to moderngl, as long as you have a machine capable of running OpenGL 4.0+, everything will work fine, no matter if you use Linux, Windows or MacOs.

Check out the package on [Pypi](https://pypi.org/project/pyperlib/)!

## How do I use Pyper?
Here is a bare-minimum example of a Pyper sketch:

```python
# pyper_example_001.py
from pyperlib import *

class MySketch(Pyper):
    def start(self):
        pass

    def update(self):
        pass
```

Run it calling:
* ```python pyper_example_001.py```

### More Examples!
We have an entire github repository dedicated to Pyper examples. [Check it out!](https://www.github.com/Canvim/Pypers/)