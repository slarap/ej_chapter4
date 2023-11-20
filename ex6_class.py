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
        return f'{self.suit}, {self.value}'
class Hand:
    def __init__(self):
        self.cards = []
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards):
        self.__cards = cards

    def cards_add(self, card):
        self.cards.append(card)

    def cards_remove(self, card_id):
        self.cards.pop(card_id)
    
    def draw(self, deck):
        card = deck.draw()
        self.cards_add(card)
    
    def discard(self, card_id):
        self.cards_remove(card_id)
    def __str__(self):
        return f'{[str(card) for card in self.cards]}'

class Deck:
    def __init__(self, Suits, Values):
        self.deck = []
        for s in Suits:
            for v in Values:
                self.deck_add(s, v)
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter
    def deck(self, cards):
        self.__deck = cards
    
    def deck_remove(self, card):
        self.deck.remove(card)
    
    def draw(self):
        return self.__deck.pop(0)
    
    def deal(self, hand, num):
        for _ in range(num):
            hand.draw(self)
    def shuffle(self):
        random.shuffle(self.deck)
    def deck_add(self, s, v):
        self.deck.append(Card(s, v))

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




    