def filter_by_state(
    operations: list[dict],
    state: str = "EXECUTED",
) -> list[dict]:
    """
    Фильтрует список операций по значению ключа 'state'.

    :param operations: Список словарей с данными операций
    :param state: Статус операции для фильтрации (по умолчанию 'EXECUTED')
    :return: Новый список словарей с указанным статусом
    """
    result = []

    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)

    return result
