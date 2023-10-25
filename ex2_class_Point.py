import math
class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.x
    def x(self, value):
        self.x = value

    @property
    def y(self):
        return self.y
    def y(self, value):
        self.y = value

    def invert_coordinates(self):
        self.x, self.y = self.y, self.x
    def __str__(self):
        return f'({self.x}, {self.y})'
    def distance_to(self, point_d):
        distancia = math.sqrt((self.x-point_d.x)**2 + (self.y-point_d.y)**2)
        return print(f'La distancia entre los dos puntos es {distancia}')