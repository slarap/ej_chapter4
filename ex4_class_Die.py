import random
class Die:
    def __init__(self, number=0, faces=6):
        self.__faces = faces
        if number == 0:
            self.__number = random.randint(1,faces)
        else:
            self.__number = number 
        
    @property
    def number(self):
        return self.__number
    def number(self,value):
        self.__number = value

    @property
    def faces(self):
        return self.__faces
    def faces(self,value):
        self.__faces = value

    def roll(self):
        self.__number = random.randint(1, self.__faces)
    
    def __str__(self):
        return f'{self.__number}'