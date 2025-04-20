from utils import calculate_percentage


class Card:
    def __init__(self, _japanese, _reading, _meaning):
        self.japanese = _japanese
        self.reading = _reading
        self.meaning = _meaning
        self.asked = 0
        self.correct_count = 0
        self.incorrect_count = 0

    def get_japanese_only(self):
        return self.japanese

    def get_japanese(self):
        return f"{self.japanese}({self.reading})"

    def get_meaning(self):
        return f"{self.meaning}"

    def mark_correct(self):
        self.asked += 1
        self.correct_count += 1

    def mark_incorrect(self):
        self.asked += 1
        self.incorrect_count += 1

    def get_stats(self):
        if self.asked == 0:
            return "N/A"
        return f"{self.correct_count}/{self.asked} {calculate_percentage(self.correct_count, self.asked)}%"

    def to_dict(self):
        result = dict()
        result["japanese"] = self.japanese
        result["reading"] = self.reading
        result["meaning"] = self.meaning
        return result

    def reset_stats(self):
        self.asked = 0
        self.correct_count = 0
        self.incorrect_count = 0
