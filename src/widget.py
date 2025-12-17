from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Обрабатывает карты и счета, возвращая строку с замаскированным номером."""

    name, number = data.rsplit(" ", 1)

    if name == "Счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Преобразует строку с датой из формата ISO в ДД.ММ.ГГГГ"""

    # Берем только дату до символа T
    date_part = date_str[:10]  # "2024-03-11"

    # Разбиваем по "-"
    year, month, day = date_part.split("-")

    # Возвращаем в нужном формате
    return f"{day}.{month}.{year}"
