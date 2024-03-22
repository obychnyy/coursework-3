import json
from datetime import datetime

def load_operations():
    with open('operations.json') as file:
        operation_list = json.load(file)
    return operation_list


def make_list(operation_list):
    x = 0
    last_list = []
    list = []
    for i in operation_list:
        if bool(i) and ((i['state'] == 'EXECUTED')):
            last_list.append(i)
    last_list.sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    while 0 <= x < len(last_list):
        if len(list) == 5:
            break
        if last_list[x]['state'] == 'EXECUTED':
            list.append(last_list[x])
        x += 1
    return list


def data_structurer(dictionary):
    date = dictionary["date"]
    type = dictionary["description"]
    currency = dictionary['operationAmount']['currency']['name']
    value = dictionary['operationAmount']['amount']
    from_where = dictionary.get('from')
    to = dictionary['to']
    return (date, type, currency, value, from_where, to)


def date_recycling(date):
    date_mas = []
    date_mas.extend([date[8:10], ".", date[5:7], ".", date[0:4]])
    new_date = ''.join(date_mas)
    return new_date


def card_recycling(from_where):
    card = []
    if from_where != None:
        if from_where[-17] == ' ':
            card.extend([from_where[0:-17], ' ', from_where[-16:-12], ' ', from_where[-12:-10], '** **** ', from_where[-4:-1], from_where[len(from_where)-1]])
            from_where = ''.join(card)
        else:
            card.extend([from_where[0: -21], ' **', from_where[-4:-1], from_where[len(from_where)-1]])
            from_where = ''.join(card)
    return from_where


def make_output(date, type_of, currency, value, from_where, to):
    dictionary = {}
    dictionary['date'] = date
    dictionary['type_of'] = type_of
    dictionary['currency'] = currency
    dictionary['value'] = value
    dictionary['from_where'] = from_where
    dictionary['to'] = to
    return dictionary
