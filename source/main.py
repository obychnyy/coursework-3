from functions import load_operations, filtered, sorter, cutter, make_output_list

operation_list = load_operations()
filtered_list = filtered(operation_list)
filtered_list = sorter(filtered_list)
filtered_list = cutter(filtered_list)
output_list = make_output_list(filtered_list)

for i in output_list:
    print(f'{i['date']} {i['type_of']}')
    if i['number_from'] is not None:
        print(f'{i['number_from']} -> {i['number_to']}')
    else:
        print(f'{i['number_to']}')
    print(f'{i['value']} {i['currency']}')
    print("")
