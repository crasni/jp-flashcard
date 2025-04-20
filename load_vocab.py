from card import Card
import json

def load_cards(filepath):
    """
    從指定的 JSON 檔案載入卡片資料。
    :param filepath: JSON 路徑（字串）
    :return: list of dicts, 每個 dict 是一張卡片
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            cards = json.load(f)
        return [Card(c["japanese"], c["reading"], c["meaning"]) for c in cards]
    except FileNotFoundError:
        print(f"找不到檔案：{filepath}")
        return []
    except json.JSONDecodeError:
        print("JSON 格式錯誤，請檢查內容")
        return []


