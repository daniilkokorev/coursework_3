import json
from config import *
from datetime import datetime


def list_operations():
    """
    Функция получает список операций из библиотеки json.
    """
    with open(OPERATIONS) as file: # читает файл json
        operations_list = json.load(file)
        return operations_list


def sort_operation_list(file_operat):
    """
    Функция отдаёт
    отформатированный, сортированный список.
    """
    operations_info = []
    full_operations = []
    for operation in file_operat:
        # перебирает список проверяя его длинну и статус выполнения операций
        if len(operation) < 1:
            continue
        elif operation['state'] == 'EXECUTED':
            operations_info.append(operation)
            # сортирует список по дате от ранней к более поздней
    short_list = sorted(operations_info, key=lambda x: datetime.strptime(x['date'],
     '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    full_operations = short_list
    return full_operations[:5]


def date_operation(operations):
    """
    Функция форматируем дату операции:
    """
    data_lists = []
    for result_oper in operations:
        # форматируем дату операции
        date_obj = datetime.fromisoformat(result_oper['date'].replace('T', ' '))
        formatted_date = date_obj.strftime("%d.%m.%Y")
        data_lists.append(formatted_date)
    return data_lists


def mask_score_number(operations):
    """
    Маскирует номер счёта "to"
    :param operations:
    :return:
    """
    score_lists = []
    for result_score in operations:
        # зашифровываем номер счёта
        number_score = result_score["to"]
        mask_score = f'{number_score[:4]} **{number_score[-4:]}'
        score_lists.append(mask_score)
    return score_lists


def mask_card_number(operations_card):
    """
    проверяем наличие ключа 'from' в словаре операции
    :param operations:
    :return:
    """
    card_masc_list = []
    for result_card in operations_card:
        if not result_card.get('from'):
            card_number = result_card['to']
        else:
            card_number = result_card["from"]
        # проверяем чем передставлен счёт карты и шифруем его
        if card_number[0] == "С":
            mask_card = f'{card_number[:4]} **{card_number[-4:]}'
            card_masc_list.append(mask_card)
        else:
            mask_card = f'{card_number[:-12]} {card_number[-10:-8]}** **** {card_number[-4:]}'
            card_masc_list.append(mask_card)
    return card_masc_list
