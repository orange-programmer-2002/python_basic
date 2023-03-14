from models.Shape import Shape

class Rect(Shape):
    
    def __init__(self, x, y, rong, dai):
        Shape.__init__(x, y)
        self.rong = rong
        self.dai = dai
        
    def chuVi(self):
        return 2 * (self.rong + self.dai)
        
    def dienTich(self):
        return self.rong * self.dai
        