import random
class Die:
    def __init__(self, number=0, faces=6):
        self.faces = faces
        if number == 0:
            self.number = random.randint(1,faces)
        else:
            self.number = number 
        
    @property
    def number(self):
        return self.number
    def number(self,value):
        self.number = value

    @property
    def faces(self):
        return self.faces
    def faces(self,value):
        self.faces = value

    def roll(self):
        self.number = random.randint(1, self.faces)
    
    def __str__(self):
        return f'{self.number}'