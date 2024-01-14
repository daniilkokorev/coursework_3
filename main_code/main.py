from functions import *


list_operation = list_operations()
operation_sort = sort_operation_list(list_operation)
date_operations = date_operation(operation_sort)
score_mask = mask_score_number(operation_sort)
card_mask = mask_card_number(operation_sort)


def operation_show(operations):
    for operation in operations:
        return (f'{date_operations} {operation["description"]}\n'
                f'{card_mask} -> {score_mask}\n'
                f'{operation["operationAmount"]["amount"]}'
                f'{operation["operationAmount"]["currency"]["name"]}\n\n')
