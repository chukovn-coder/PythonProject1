import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура с тестовыми транзакциями
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "US Dollar", "code": "USD"},
            },
            "description": "Перевод USD",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "Euro", "code": "EUR"},
            },
            "description": "Перевод EUR",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"name": "US Dollar", "code": "USD"},
            },
            "description": "Еще перевод USD",
        },
    ]


# Тесты для filter_by_currency
# Проверка фильтрации
def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(
        transaction["operationAmount"]["currency"]["code"] == "USD"
        for transaction in result
    )


# Нет подходящей валюты
def test_filter_by_currency_not_found(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "GBP"))
    assert result == []


# Пустой список
def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


# Тесты для transaction_descriptions
# Обычный случай
def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод USD",
        "Перевод EUR",
        "Еще перевод USD",
    ]


# Пустой список
def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


# Тесты для card_number_generator
# Проверка диапазона
def test_card_number_generator_range():
    result = list(card_number_generator(1, 3))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


# Параметризация
@pytest.mark.parametrize(
    "start,end,expected_first,expected_last",
    [
        (1, 1, "0000 0000 0000 0001", "0000 0000 0000 0001"),
        (9, 10, "0000 0000 0000 0009", "0000 0000 0000 0010"),
        (9999, 10000, "0000 0000 0000 9999", "0000 0000 0001 0000"),
    ],
)
def test_card_number_generator_parametrized(
    start, end, expected_first, expected_last
):
    result = list(card_number_generator(start, end))
    assert result[0] == expected_first
    assert result[-1] == expected_last
