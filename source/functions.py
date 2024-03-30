import json
from datetime import datetime


def load_operations():
    with open('operations.json') as file:
    return json.load(file)

def filter(operation_list: list[dict]) -> list[dict]:
    filtred_list = []
    for i in operation_list:
        if i['state'] == 'EXECUTED':
            filtred_list.append(i)
    return filtred_list


def sorting(filtred_list: list[dict]) -> list[dict]:
    return filtred_list.sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse = True)


def cutter(filtred_list: list[dict]) -> list[dict]:
    return filtred_list[:5]



def data_structurer(dictionary):
    date = dictionary["date"]
    type = dictionary["description"]
    currency = dictionary['operationAmount']['currency']['name']
    value = dictionary['operationAmount']['amount']
    from_where = dictionary.get('from')
    to = dictionary['to']
    return (date, type, currency, value, from_where, to)


def date_recycling(date):
    date = datetime.fromisoformat(date, '%d.%m.%Y')
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
