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
    for operation in file_operat:
        # перебирает список проверяя его длинну и статус выполнения операций
        if len(operation) < 1:
            continue
        elif operation['state'] == 'EXECUTED':
            operations_info.append(operation)
            # сортирует список по дате от ранней к более поздней
    short_list = sorted(operations_info, key=lambda x: datetime.strptime(x['date'],
     '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return short_list[:5]


def report_operation(operations):
    """
    Функция выводит отформатированный отчёт по операциям:
    - форматируе дату;
    - шифрует счёт и номер карты
    """
    info_operat = ""
    for result_oper in operations:
        # форматируем дату операции
        date_obj = datetime.fromisoformat(result_oper['date'].replace('T', ' '))
        formatted_date = date_obj.strftime("%d.%m.%Y")
        # зашифровываем номер счёта
        number_score = result_oper["to"]
        mask_score = f'{number_score[:4]} **{number_score[-4:]}'
        # проверяем наличие ключа 'from' в словаре операции
        if not result_oper.get('from'):
            card_number = result_oper["to"]
        else:
            card_number = result_oper["from"]
        # проверяем чем передставлен счёт карты и шифруем его
        if card_number[0] == "С":
            mask_card = f'{card_number[:4]} **{card_number[-4:]}'
        else:
            mask_card = f'{card_number[:-12]} {card_number[-10:-8]}** **** {card_number[-4:]}'
        # формируем корректный вывод данных по операции
        info_operat += (f'{formatted_date} {result_oper["description"]}\n'
                        f'{mask_card} -> {mask_score}\n'
                        f'{result_oper["operationAmount"]["amount"]} '
                        f'{result_oper["operationAmount"]["currency"]["name"]}\n\n')
    return info_operat
