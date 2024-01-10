import json
from datetime import datetime


def data_operations():
    """
    получает список операций
    """
    operations_info = []
    with open('operations.json') as file:
        operations_list = json.load(file)
        for operation in operations_list:
            if len(operation) < 1 or operation['state'] == 'CANCELED' or not operation.get('from'):
                continue
            else:
                operations_info.append(operation)
        short_list = sorted(operations_info, key=lambda x: datetime.strptime(x['date'],
        '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
        return short_list

new_operat_list = data_operations()

def report_operation():
    info_operat = ""
    for result_oper in new_operat_list[:5]:
        date_obj = datetime.fromisoformat(result_oper['date'].replace('T', ' '))
        formatted_date = date_obj.strftime("%d.%m.%Y")
        card_number = result_oper["from"]
        if card_number[0] == "С":
            mask_card = f'{card_number[:4]} **{card_number[-4:]}'
        else:
            mask_card = f'{card_number[:-12]} {card_number[-10:-8]}** **** {card_number[-4:]}'
        number_score = result_oper["to"]
        mask_score = f'{number_score[:4]} **{number_score[-4:]}'
        info_operat += (f'{formatted_date} {result_oper["description"]}\n'
                        f'{mask_card} -> {mask_score}\n'
                        f'{result_oper["operationAmount"]["amount"]} '
                        f'{result_oper["operationAmount"]["currency"]["name"]}\n\n')
    return info_operat



print(report_operation())
