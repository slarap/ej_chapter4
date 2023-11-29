from ex6_class import Card, Hand, SpanishDeck, EnglishDeck

print("Test creación carta")
card1 = Card("Bastos", 5)
print(card1)

print("Test creación mano")
mano1 = Hand()

print("Test creación baraja")
baraja_spanish = SpanishDeck()


print("Repartir cartas a la mano")
baraja_spanish.deal(mano1, 5)
print(mano1)

print("Robar una carta del mazo")
mano1.draw(baraja_spanish)
print(mano1)

print("Empezar un juego")
baraja_juego = SpanishDeck()
mano_juego = Hand()
baraja_juego.shuffle()
baraja_juego.deal(mano_juego, 5)
print(mano_juego)

mano_juego.draw(baraja_juego)
print(mano_juego)

mano_juego.discard(3, baraja_juego)
print(mano_juego)