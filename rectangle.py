class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.width

    def getArea(self):
        return self.width * self.height

from rectangle import Rectangle

r1 = Rectangle(10,5)

print('r1.width= ', r1.width)
print('r1.height= ', r1.height)
print('r1.getWidth= ', r1.getWidth())
print('r1.getArea= ', r1.getArea())

print((5+6)*(7+8)/(4+3))