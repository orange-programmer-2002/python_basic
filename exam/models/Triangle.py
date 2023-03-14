import math

from models.Shape import Shape

class Triangle(Shape):
    
    def __init__(self, x, y, a, b, c):
        Shape.__init__(x, y)
        self.a = a
        self.b = b
        self.c = c
        
    def chuVi(self):
        return self.a + self.b + self.c
    
    def dienTich(self):
        p = self.chuVi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))