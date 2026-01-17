import pytest
from src.masks import get_mask_card_number


# ТЕСТЫ ДЛЯ get_mask_card_number
def test_get_mask_card_number_basic():
    """Проверка стандартного маскирования номера карты"""
    card_number = "7000792289606361"

    result = get_mask_card_number(card_number)

    assert result == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("9999888877776666", "9999 88** **** 6666"),
    ],
)
def test_get_mask_card_number_parametrized(card_number: str, expected: str):
    """Проверка маскирования номера карты с разными входными данными"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty_string():
    from src.masks import get_mask_card_number

    result = get_mask_card_number("")
    assert result == " ** **** "


def test_get_mask_card_number_without_digits():
    from src.masks import get_mask_card_number

    result = get_mask_card_number("Visa Platinum")
    assert result == "Visa  P** **** inum"


# ТЕСТЫ ДЛЯ get_mask_account
from src.masks import get_mask_account


def test_get_mask_account_basic():
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678123456787894", "**7894"),
        ("99998888777766665555", "**5555"),
        ("1234", "**1234"),
        ("12", "**12"),
    ],
)
def test_get_mask_account_various_lengths(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_empty_string():
    assert get_mask_account("") == "**"
