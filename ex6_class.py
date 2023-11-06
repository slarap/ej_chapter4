class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit):
        if suit in ["'Hearts', 'Diamonds', 'Clubs', 'Spades'"]:
            self.__suit = suit
        else:
            raise TypeError("Suit or value is not valid")
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if value in range(1,10) or value in ["J", "Q", "K"]:
            self.__value = value
        else:
            raise TypeError("Suit or value is not valid")
class Hand():
    def __init__(self):
        self.cards=[]
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, card):
        self.cards.append(card)