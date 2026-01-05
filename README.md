# PythonProject1

## Описание: 
Данный проект является учебным и предназначен для отработки навыков работы с Python, Git и GitHub, а также инструментов статического анализа и форматирования кода.

Проект реализует функции для:

маскировки номеров банковских карт и счетов;

обработки списка банковских операций;

фильтрации операций по статусу;

сортировки операций по дате.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:chukovn-coder/PythonProject1.git
```
2. Установите зависимости с помощью Poetry:

poetry install

3. Активируйте виртуальное окружение:

poetry shell

## Использование:

1. Маскировка карт и счетов

Функция mask_account_card находится в модуле widget и принимает строку с типом и номером карты или счета.

from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))

=> Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))

=> Счет **4305

2. Фильтрация операций по статусу

Функция filter_by_state находится в модуле processing и возвращает список операций с указанным статусом.

from src.processing import filter_by_state


operations = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
]


print(filter_by_state(operations))

=> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

3. Сортировка операций по дате

Функция sort_by_date находится в модуле processing и сортирует список операций по дате.
По умолчанию сортировка выполняется по убыванию (сначала самые новые операции).

from src.processing import sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
]

print(sort_by_date(operations))

=> [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
]

4. Маскировка номера банковской карты

Функция get_mask_card_number находится в модуле masks и маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))

=> 7000 79** **** 6361

5. Маскировка номера банковского счета

Функция get_mask_account находится в модуле masks и маскирует номер банковского счета, показывая только последние 4 цифры.

from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))

=> **4305

6. Преобразование даты

Функция get_date находится в модуле widget и преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))

=> 11.03.2024

## Технологии

- Python 3.14
- Poetry
- Flake8
- Black
- isort
- mypy
- Git / GitHub
