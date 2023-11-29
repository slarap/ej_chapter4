#pop es para sacar por indice
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit):
        self.__suit = suit
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value
    def __str__(self):
        return f'{self.value} de {self.suit}'
    
class Hand:
    def __init__(self):
        self.cards = []
    @property
    def cards(self):
        return self.__cards
    
    @cards.setter
    def cards(self, value):
        self.__cards = value

    def draw(self, deck): 
        self.cards.append(deck.draw())

    def discard(self, posicion, deck):
        card = self.cards[posicion]
        self.cards.remove(card)
        deck.deck_add(card)

    def __str__(self):
        cadena = ""
        for card in self.cards:
            cadena += f'{card} // '
        return cadena
       

class Deck:
    def __init__(self, Suits, Values):
        self.deck = []
        for s in Suits:
            for v in Values:
                card = Card(s, v)
                self.deck_add(card)
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter
    def deck(self, cards):
        self.__deck = cards
    
    def draw(self):
        card = self.__deck.pop(0)
        return card
    
    def deal(self, hand, num):
        for _ in range(num):
            hand.draw(self)

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deck_add(self, card):
        self.deck.append(card)

class SpanishDeck(Deck):
    suits = ["Oros", "Copas", "Espadas", "Bastos"]
    values = ["A","2","3","4","5","6","7","8","9","10","11","12"]
    def __init__(self):
        super().__init__(self.suits, self.values)

class EnglishDeck(Deck):
    suits = ["Picas", "Rombos", "Tréboles", "Diamantes"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        super().__init__(self.suits, self.values)