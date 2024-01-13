from functions import *


list_operation = list_operations()
operation_sort = sort_operation_list(list_operation)
date_operations = date_operation(operation_sort)
score_mask = mask_score_number(operation_sort)
card_mask = mask_card_number(operation_sort)

for operation in operation_sort:
    print(f'{date_operations} {operation["description"]}')
    print(f'{card_mask} -> {score_mask}')
    print(f'{operation["operationAmount"]["amount"]}'
          f'{operation["operationAmount"]["currency"]["name"]}\n')
