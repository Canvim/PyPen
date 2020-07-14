import colorsys


class Color:
    def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0, rgba_tuple=None):
        if rgba_tuple:
            if len(rgba_tuple) == 3:
                self.r, self.g, self.b = rgba_tuple
                self.a = a
            else:
               self.r, self.g, self.b, self.a = rgba_tuple 
        else:
            self.r = r
            self.g = g
            self.b = b
            self.a = a
            
    
    def rgb(self):
        return self.r, self.g, self.b
    
    def rgba(self):
        return self.r, self.g, self.b, self.a

    @classmethod
    def from_rgb(cls, r: float, g: float, b: float):
        return cls(r, g, b)

    @classmethod
    def from_rgba(cls, r: float, g: float, b: float, a: float):
        return cls(r, g, b, a)
    
    @classmethod
    def from_hsv(cls, h: float, s: float, v: float):
        return cls(rgba_tuple=colorsys.hsv_to_rgb(h, s, v))
    
    @classmethod
    def from_hls(cls, h: float, l: float, s: float):
        return cls(rgba_tuple=colorsys.hls_to_rgb(h, l, s))


class Colors:
    def __init__(self):
        self.default_background_color = Color.from_rgb(0.0, 0.0, 0.0)
        self.default_color = Color.from_rgb(0.2, 0.4, 0.5)

        self.red = Color.from_rgb(0.8, 0.2, 0.2)
        self.green = Color.from_rgb(0.2, 0.8, 0.2)
        self.blue = Color.from_rgb(0.2, 0.2, 0.8)

        self.dark_green = Color.from_rgb(0.097, 0.613, 0.207)


colors = Colors()
