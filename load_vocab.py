from card import Card
import json


def load_cards(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            cards = json.load(f)
        return [Card(c["japanese"], c["reading"], c["meaning"]) for c in cards]
    except FileNotFoundError:
        print(f"File not found：{filepath}")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []
