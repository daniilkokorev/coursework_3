from functions import *


list_operation = list_operations()
operation_sort = sort_operation_list(list_operation)
date_operations = date_operation(operation_sort)
score_mask = mask_score_number(operation_sort)
card_mask = mask_card_number(operation_sort)


for operation in range(len(operation_sort)):
    print(f'{date_operations[operation]} {operation_sort[operation]["description"]}')
    print(f'{card_mask[operation]} -> {score_mask[operation]}')
    print(f'{operation_sort[operation]["operationAmount"]["amount"]}'
          f'{operation_sort[operation]["operationAmount"]["currency"]["name"]}\n')
