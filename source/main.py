import functions

output_list = []
operation_list = functions.load_operations()
list_of = functions.make_list(operation_list)

for i in list_of:
    date, type_of, currency, value, from_where, to = functions.data_structurer(i)
    date = functions.date_recycling(date)
    from_where = functions.card_recycling(from_where)
    to = functions.card_recycling(to)
    dictionary = functions.make_output(date, type_of, currency, value, from_where, to)
    output_list.append(dictionary)

for i in output_list:
    print(f'{i['date']} {i['type_of']}')
    if i['from_where'] != None:
        print(f'{i['from_where']} -> {i['to']}')
    else:
        print(f'{i['to']}')
    print(f'{i['value']} {i['currency']}')
    print("")
