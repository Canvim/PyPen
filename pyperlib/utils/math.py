import math

def clamp(value, min, max):
    return (value <= min)*min + (value >= max)*max + value*(value > min and value < max)

def lerp_unclamped(start, end, t):
    return start + t*(end-start)

def lerp(start, end, t):
    value = lerp_unclamped(start, end, t)
    return clamp(value, start, end)
