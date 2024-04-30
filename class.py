class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
class Circle(Point):
    def __init__(self,x, y , r):
        super().__init__(x, y)
        self.r = r
        # g
    def Area(self):
        return 2 * 3.14 * (self.r)
    def perime (self):
        return 3.14*(self.r*self.r)
class cylinder(Circle):
    def __init__(self, x, y, r,h):
        super().__init__(x, y , r)
        self.h=h
    def s(self):
        return (2 * self.Area()) + (self.perime() * self.h)
c = cylinder(3,4,5,6)
print(cylinder.s(c))