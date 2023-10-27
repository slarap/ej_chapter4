from ex4_class_Die import Die
die1 = Die(2, 7)
die2 = Die(4, 4)
die3 = Die(3, 12)
die4= Die(5, 6)
for i in range(3):
    die1.roll()
    die2.roll()
    die3.roll()
    die4.roll()
    print(die1, die2, die3, die4)
