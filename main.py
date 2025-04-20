from load_vocab import load_cards
from flashcard_engine import FlashcardEngine

cards = load_cards("vocab/lesson10/lesson10.json")
instance = FlashcardEngine(cards)

instance.start_quiz(7, True, False)
