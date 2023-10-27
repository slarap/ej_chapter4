import random
class Dice:
    def __init__(self):
        self.__number = None
    def roll(self):
        self.__number = random.randint(1,6)
        return self.__number
