from utils import calculate_percentage


class Card:
    def __init__(self, _japanese, _reading, _meaning, _asked=0, _ccnt=0, _icnt=0):
        self.japanese = _japanese
        self.reading = _reading
        self.meaning = _meaning
        self.asked = _asked
        self.correct_count = _ccnt
        self.incorrect_count = _icnt

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
        result["asked"] = self.asked
        result["correct_count"] = self.correct_count
        result["incorrect_count"] = self.incorrect_count
        return result

    def reset_stats(self):
        self.asked = 0
        self.correct_count = 0
        self.incorrect_count = 0
