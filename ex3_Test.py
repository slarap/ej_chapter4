from ex2_class_Point import Point
from ex3_class_rectangle import Rectangle
point1 = Point(2, 8)
point2 = Point(1, 5)
rectangle = Rectangle(point1, point2)
print(f'El area del rectángulo es {rectangle.area()}')
print(f'El perímetro del rectángulo es {rectangle.perimetro()}')