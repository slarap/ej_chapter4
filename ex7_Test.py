from ex7_class import Card, Hand, EnglishDeck, Player, BlackjackGame

juego = BlackjackGame("Sebas", "Pedro")

juego.new_game()
juego.dealer_hit()
print(juego.player.hand)
print(juego.player.hand.total_value())
juego.player_hit()
print(juego.player.hand)
print(juego.player.hand.total_value())
print(juego.end_game())
