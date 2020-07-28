## [<- Back](https://github.com/Canvim/PyPen)

# How do I use PyPen?
## 1. Install PyPen
To install pypen, make sure you have Python 3.8 or higher installed as well as pip configured and available in your PATH. Once that's done, simply do **```pip install pypen```**. To verify that it was installed correctly, run **```pypen --version```** (or ```python -m pypen --version```) and it should display the current version of PyPen.

Since Cairo - one of PyPen's dependencies - sometimes can be a bit tricky to install, see our OS-specific instructions available here:
* [Windows](./WINDOWS.md)
* [MacOS](./MACOS.md)
* [Linux](./LINUX.md)

## 2. Create a PyPen Sketch
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

## 3. Run Your Sketch!
You can then run it by simply calling:
- **```pypen pypen_example.py```**
- (or ```python -m pypen pypen_example.py```)

## 4. Profit!
If everything worked, a window should launch containing something looking like this:

<img src="https://i.imgur.com/AwMJM3K.png" width="200px">

Wohoo! You made it! You have now launched your first PyPen sketch! Try changing some variables like the color from ```"red"``` to ```"blue"``` or the width and height of the rectangle (or maybe even change it into a circle!).

## 5. What now?
There is much more that PyPen can do that you have yet to discover. Interested in seeing how simple it is to use PyPen? We have an entire folder filled with interesting PyPen examples spanning from very simple to some more advanced ones as well. You find them in the 'examples/' folder on our repository located here:

## **[Examples](../examples/)**

You can also refer to our documentation available here:

## **[Documentation](../examples/)**