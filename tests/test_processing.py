import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    """Фикстура со списком банковских операций"""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 4,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


# ТЕСТЫ ДЛЯ filter_by_state
# Проверка значения по умолчанию (EXECUTED)
def test_filter_by_state_default(operations):
    """Фильтрация по статусу EXECUTED по умолчанию"""
    result = filter_by_state(operations)

    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


# ТЕСТ Параметризация по разным статусам
@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
    ],
)
def test_filter_by_state_parametrized(operations, state, expected_count):
    """Фильтрация по разным статусам"""
    result = filter_by_state(operations, state)

    assert len(result) == expected_count
    assert all(item["state"] == state for item in result)


# ТЕСТ Нет операций с таким статусом
def test_filter_by_state_no_matches(operations):
    """Если операций с таким статусом нет — возвращается пустой список"""
    result = filter_by_state(operations, "PENDING")

    assert result == []


# ТЕСТ ДЛЯ sort_by_date
# Сортировка по убыванию (по умолчанию)
def test_sort_by_date_descending(operations):
    """Сортировка по дате по убыванию"""
    result = sort_by_date(operations)

    dates = [item["date"] for item in result]

    assert dates == sorted(dates, reverse=True)


# ТЕСТ Сортировка по возрастанию
def test_sort_by_date_ascending(operations):
    """Сортировка по дате по возрастанию"""
    result = sort_by_date(operations, False)

    dates = [item["date"] for item in result]

    assert dates == sorted(dates)


# ТЕСТ Одинаковые даты (граничный случай)
def test_sort_by_date_same_dates():
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2020-01-01T00:00:00"},
    ]

    result = sort_by_date(operations)

    assert len(result) == 2
