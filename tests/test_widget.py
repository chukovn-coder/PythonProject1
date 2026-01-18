import pytest

from src.widget import get_date, mask_account_card


# ТЕСТ mask_account_card НА СЧЕТ
def test_mask_account_card_account():

    result = mask_account_card("Счет 73654108430135874305")

    assert result == "Счет **4305"


# ТЕСТ mask_account_card НА КАРТУ
def test_mask_account_card_card():

    result = mask_account_card("Visa Platinum 7000792289606361")

    assert result == "Visa Platinum 7000 79** **** 6361"


# Параметризация mask_account_card
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card_parametrized(input_data, expected):
    assert mask_account_card(input_data) == expected


# ТЕСТ НА ПУСТУЮ СТРОКУ
def test_mask_account_card_empty_string():
    assert mask_account_card("") == ""


# ТЕСТ НА СТРОКУ БЕЗ ЦИФР
def test_mask_account_card_without_digits():
    assert mask_account_card("Visa Platinum") == "Visa Platinum"


# ТЕСТ НА СТРОКУ БЕЗ ТИПА
def test_mask_account_card_only_number():
    assert mask_account_card("7000792289606361") == "7000792289606361"


# ТЕСТЫ ДЛЯ get_date
def test_get_date_basic():

    date_str = "2019-07-03T18:35:29.512364"

    result = get_date(date_str)

    assert result == "03.07.2019"


# ТЕСТЫ ПАРАМЕТРИЗАЦИЯ ДЛЯ get_date
@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2023-08-15T10:20:30.123456", "15.08.2023"),
    ],
)
def test_get_date_parametrized(input_date: str, expected: str):
    assert get_date(input_date) == expected


# Тесты для get_data ПУСТАЯ СТРОКА
def test_get_date_empty_string():
    assert get_date("") == ""


# Тесты для get_data СРОКА БЕЗ ДАТЫ
def test_get_date_without_date():
    assert get_date("not a date") == "not a date"
