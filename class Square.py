class Square:
    def __init__(self, side):
        self.side = side


class Triangle(Square):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def Pyramid(self):
        return (4) * (1 / 2) * (self.side) * (self.height) + (self.side * self.side)


The_Pyramid = Triangle(int(input('Please enter your side: ')) , int(input('Please enter your height: ')))
print(The_Pyramid.Pyramid())
