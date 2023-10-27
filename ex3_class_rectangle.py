from ex2_class_Point import Point
class Rectangle:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2
    def area(self):
        return abs(self.__point2.x-self.__point1.x) * abs(self.__point2.y-self.__point1.y)
    def perimetro(self):
        return (abs(self.__point2.x-self.__point1.x)+abs(self.__point2.y-self.__point1.y))*2