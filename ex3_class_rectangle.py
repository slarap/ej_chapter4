from ex2_class_Point import Point
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def area(self):
        base = abs(self.point2.x-self.point1.x)
        altura = abs(self.point2.y-self.point1.y)
        a = base*altura
        return a
    def perimetro(self):
        base = abs(self.point2.x-self.point1.x)
        altura = abs(self.point2.y-self.point1.y)
        p = (base + altura)*2
        return p
    