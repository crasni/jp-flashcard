from card import Card
import json

def load_cards(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            cards = json.load(f)
        return [Card(c["japanese"], c["reading"], c["meaning"]) for c in cards]
    except FileNotFoundError:
        print(f"Unable to find file：{filepath}")
        return []
    except json.JSONDecodeError:
        print("JSON format error")
        return []
