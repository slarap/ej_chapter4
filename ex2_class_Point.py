import math
class Point:
    def __init__(self, x=0,y=0):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.__x = value
        else:
            raise TypeError (f'{value} no es un entero.')

    @property
    def y(self):
        return self.__y
    @x.setter
    def y(self, value):
        self.__y = value

    def invert_coordinates(self):
        self.__x, self.__y = self.__y, self.__x
    def __str__(self):
        return f'({self.__x}, {self.__y})'
    def distance_to(self, point_d):
        return math.sqrt((self.__x-point_d.x)**2 + (self.__y-point_d.y)**2)