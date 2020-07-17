from math import sin, cos, tan
from math import asin, acos, atan
from math import sinh, cosh, tanh
from math import asinh, acosh, atanh
from math import atan2

from math import sqrt

from math import pi as PI
from math import tau as TAU
from math import e as E


def clamp(value, min, max):
    return (value <= min)*min + (value >= max)*max + value*(value > min and value < max)


def lerp_unclamped(start, end, t):
    return start + t*(end-start)


def lerp(start, end, t):
    value = lerp_unclamped(start, end, t)
    return clamp(value, start, end)


def mix(a, b, t):
    return lerp(a, b, t)
