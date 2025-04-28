from card import Card
from utils import calculate_percentage
import random as r


class FlashcardEngine:
    def __init__(self, _qpool: list[Card]):
        self.question_pool = _qpool

    def ask_card(self, c: Card, jp_only: bool):
        input_msg = ""
        if jp_only:
            input_msg = c.get_japanese_only()
        else:
            input_msg = c.get_japanese()
        response = input(f"{input_msg} (y/n): ")

        if response == "y":
            c.mark_correct()
        else:
            c.mark_incorrect()
        print(f"→ {c.get_meaning()} | Accuracy: {c.get_stats()}")

        return response == "y"

    def reset_question_pool(self):
        for c in self.question_pool:
            c.reset_stats()

    def start_quiz(self, amount=10, shuffle: bool = True, jp_only: bool = False):
        tmp = self.question_pool.copy()
        if shuffle:
            r.shuffle(tmp)
        correct = 0
        for i in range(amount):
            card = tmp[i]
            if self.ask_card(card, jp_only):
                correct += 1

        print(f"In this session, you've been asked {amount} vocabularies.")
        print(f"You got {correct}/{amount} {calculate_percentage(correct, amount)}%")
