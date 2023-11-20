from ex6_class import Card, Hand, SpanishDeck, EnglishDeck

print("Test creación carta")
card1 = Card("Bastos", 5)
print(card1)

print("Test creación baraja")
baraja = SpanishDeck()
print(baraja.draw())
print(baraja.draw())
baraja.shuffle()
print(baraja.draw())

print("Test creación baraja inglesa")
baraja_ing = EnglishDeck()
print(baraja_ing.draw())
print(baraja_ing.draw())
baraja_ing.shuffle()
print(baraja_ing.draw())

print("Test mano")
mano = Hand()
baraja_mano = SpanishDeck()
baraja_mano.deal(mano, 5)
print(baraja_mano.draw())
print(mano)

print("Test mano y baraja")
mano2 = Hand()
baraja_test = SpanishDeck()
baraja_mano.shuffle()
baraja_mano.deal(mano2, 10)
print(mano2)