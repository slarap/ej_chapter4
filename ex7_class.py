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
    
    def total_value(self):
        valor_total = 0
        ace = 0
        for i in self.cards:
            if i.value in ["J", "Q", "K"]:
                valor_total += 10
            elif i.value == "A":
                valor_total += 11
                ace += 1
            else:
                valor_total += i.value
            if valor_total > 21 and ace > 0:
                while valor_total > 21:
                    for _ in range(ace):
                        valor_total -= 10 
        return valor_total


    def __str__(self):
        cadena = ""
        for card in self.cards:
            cadena += f'{card} // '
        return cadena
       

class Deck:
    def __init__(self, suits, values):
        self.deck = []
        for s in suits:
            for v in values:
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

class EnglishDeck(Deck):
    suits = ["Picas", "Rombos", "Tréboles", "Diamantes"]
    values = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    def __init__(self):
        super().__init__(self.suits, self.values)

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, hand):
        self.__hand = hand
    
    def __str__(self):
        return print(f'{self.name} tiene las cartas {self.hand}')

class BlackjackGame:
    def __init__(self, player_name: str, dealer_name: str):
        self.deck = "Inglesa"
        self.player = player_name
        self.dealer = dealer_name
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter
    def deck(self, deck):
        if deck == "Inglesa":
            self.__deck = EnglishDeck()
            self.__deck.shuffle()
    
    @property
    def player(self):
        return self.__player
    
    @player.setter
    def player(self, player_name):
        self.__player = Player(player_name)

    @property
    def dealer(self):
        return self.__dealer
    
    @dealer.setter
    def dealer(self, dealer_name):
        self.__dealer = Player(dealer_name)
    
    def new_game(self):
        self.deck.deal(self.player.hand, 2)
        self.deck.deal(self.dealer.hand, 2)
    
    def player_hit(self):
            self.player.hand.draw(self.deck)

    def dealer_hit(self):
        while self.dealer.hand.total_value() < 16:
            self.dealer.hand.draw(self.deck)
        else:
            None

    def end_game(self):
        if self.player.hand.total_value() > 21:
            return f'Te has pasado. Has perdido.'
        elif self.dealer.hand.total_value()>21:
            return f'El dealer ha perdido. Has ganado.'
        elif self.player.hand.total_value() > self.dealer.hand.total_value():
            return f'Tus cartas ({self.player.hand.total_value()}) son mayores que las del dealer ({self.dealer.hand.total_value()}). Has ganado'
        else:
            return f'Has perdido. Las cartas del dealer ({self.dealer.hand.total_value()}) son mayores que las tuyas ({self.player.hand.total_value()}).'
        
        