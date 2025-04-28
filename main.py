import vocab_io
from flashcard_engine import FlashcardEngine

cards = vocab_io.load_cards("vocab/lesson10/lesson10.json")
if not cards:
    exit(-1)
instance = FlashcardEngine(cards)

while input("Start quiz? (y/n) ") == "y":
    instance.start_quiz(7, True, False)

want_reset = input("Reset all cards' stats? (y/n) ")
if want_reset == "y":
    instance.reset_question_pool()

vocab_io.save_cards("vocab/lesson10/lesson10.json", cards)
