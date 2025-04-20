from load_vocab import load_cards

cards = load_cards("vocab/lesson10/lesson10.json")

for card in cards:
    card.show_japanese()
    card.show_meaning()

