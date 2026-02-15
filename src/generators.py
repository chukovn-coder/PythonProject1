from typing import Iterator


def filter_by_currency(
    transactions: list[dict],
    currency_code: str
) -> Iterator[dict]:
    """Принимает на вход список словарей,
представляющих транзакции."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Принимает список словарей с транзакциями
и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Выдает номера банковских карт в формате
XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        # превращаем число в строку из 16 цифр с ведущими нулями
        card_number = f"{number:016d}"

        # разбиваем на группы по 4 цифры
        formatted = " ".join(
            card_number[i:i + 4] for i in range(0, 16, 4)
        )

        yield formatted
