import colorsys

_COLORS = {
    "default_background_color" : (0),
    "default_color" : (30, 60, 125),
    "red" : (200, 30, 30),
    "green" : (30, 200, 30),
    "blue" : (30, 30, 200)
}

class Color:
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = int(a)

    def rgb(self):
        return self.r, self.g, self.b

    def rgba(self):
        return self.r, self.g, self.b, self.a
    
    @classmethod
    def from_user_input(cls, user_input):
        if type(user_input) is Color:
            return user_input
            
        if type(user_input) is tuple:
            if len(user_input) == 1 or len(user_input) == 3:
                r, g, b = user_input
                return cls(r, g, b)
            
            if len(user_input) == 4:
                r, g, b, a = user_input
                return cls(r, g, b, a)
        
        if type(user_input) is str:
            if user_input in _COLORS.keys():
                return Color.from_user_input(_COLORS[user_input])

        return cls()
