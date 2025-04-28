from card import Card
import json


def load_cards(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            cards = json.load(f)
        return [Card(c["japanese"], c["reading"], c["meaning"], c.get("asked", 0),
                     c.get("correct_count", 0), c.get("incorrect_count", 0)) for c in cards]
    except FileNotFoundError:
        print(f"File not found：{filepath}")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []


def save_cards(filepath, cards):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump([c.to_dict() for c in cards], f, ensure_ascii=False, indent=2)
        return True
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return False
    except Exception:
        raise Exception
