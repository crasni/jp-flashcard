def calculate_percentage(correct: int, total: int) -> str | float:
    if total == 0:
        return "N/A"
    return round(correct / total, 4) * 100
