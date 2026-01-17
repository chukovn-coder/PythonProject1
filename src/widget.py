from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Обрабатывает карты и счета, возвращая строку с замаскированным номером."""

    if not data:
        return ""

    if not any(char.isdigit() for char in data):
        return data

    if " " not in data:
        return data

    name, number = data.rsplit(" ", 1)

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Преобразует строку с датой из формата ISO в ДД.ММ.ГГГГ"""

    if not date_str or "-" not in date_str:
        return date_str

    date_part = date_str[:10]

    parts = date_part.split("-")
    if len(parts) != 3:
        return date_str

    year, month, day = parts
    return f"{day}.{month}.{year}"
