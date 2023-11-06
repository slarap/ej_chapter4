class Card:
    def __init__(self, suit, value):
        if suit in ["'Hearts', 'Diamonds', 'Clubs', 'Spades'"]:
            self.__suit = suit
        if value in range(1,10) or suit in ["J", "Q", "K"]:
            self.__value = value
        else:
            raise TypeError("Suit or value is not valid")
class Hand:
    