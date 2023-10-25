import random
class Dice:
    def __init__(self):
        self.number = None
    def roll(self):
        self.number = random.randint(1,6)
        return self.number

dice1 = Dice()
dice2 = Dice()
for i in range(5):
    print(f'{dice1.roll()} & {dice2.roll()}')
