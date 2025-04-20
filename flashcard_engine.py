from card import Card
import random as r


class FlashcardEngine:
    def __init__(self, _qpool: list[Card]):
        self.question_pool = _qpool

    def ask_card(self, c: Card):
        response = input(f"{c.get_japanese()} (y/n): ")
        if response == "y":
            c.mark_correct()
        else:
            c.mark_incorrect()
        print(f"{c.get_meaning()}   Accuracy: {c.get_stats()}")

        return response == "y"

    def start_quiz(self, amount = 10, shuffle: bool = True):
        tmp = self.question_pool.copy()
        if shuffle:
            r.shuffle(tmp)
        correct = 0
        for _ in range(amount):
            random_idx = r.randint(0, len(tmp) - 1)
            if self.ask_card(tmp[random_idx]):
                correct += 1

        print(f"In this session, you've been asked {amount} vocabularies.")
        print(f"You got {correct}/{amount} {round(correct/amount, 4) * 100}%")
