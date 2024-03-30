import json
from datetime import datetime


def load_operations():
    with open('../operations.json') as file: #
        return json.load(file)


def filter(operation_list: list[dict]) -> list[dict]:
    '''
    creates a list of dictionaries of only completed operations
    :param operation_list: list[dict]
    :return filtred_list: list[dict]
    '''
    filtred_list = []
    for i in operation_list:
        if i and i['state'] == 'EXECUTED':
            filtred_list.append(i)
    return filtred_list


def sorter(filtred_list: list[dict]) -> list[dict]:
    filtred_list.sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse = True)
    return filtred_list


def cutter(filtred_list: list[dict]) -> list[dict]:
    x = 0
    cutted_list = []
    while x < 5:
        cutted_list.append(filtred_list[x])
        x += 1
    return cutted_list


def data_structurer(dictionary):
    date = dictionary["date"]
    type = dictionary["description"]
    currency = dictionary['operationAmount']['currency']['name']
    value = dictionary['operationAmount']['amount']
    from_where = dictionary.get('from')
    to = dictionary['to']
    return date, type, currency, value, from_where, to


def make_output_list(filtred_list: list[dict]) -> list[dict]:
    output_list = []
    for i in filtred_list:
        date, type_of, currency, value, from_where, to = data_structurer(i)
        date = date_recycling(date)
        from_where = card_recycling(from_where)
        to = card_recycling(to)
        dictionary = make_output(date, type_of, currency, value, from_where, to)
        output_list.append(dictionary)
    return output_list


def date_recycling(date: str) -> str:
    date = datetime.fromisoformat(date)
    return date.strftime('%d.%m.%Y')


def card_recycling(from_where):
    card = []
    if from_where is not None:
        if from_where[-17] == ' ':
            card.extend([from_where[0:-17], ' ', from_where[-16:-12], ' ', from_where[-12:-10], '** **** ', from_where[-4:-1], from_where[len(from_where)-1]])
            from_where = ''.join(card)
        else:
            card.extend([from_where[0: -21], ' **', from_where[-4:-1], from_where[len(from_where)-1]])
            from_where = ''.join(card)
    return from_where


def make_output(date: str, type_of: str, currency: str, value: str, from_where: str or None, to: str) -> dict:
    dictionary = {}
    dictionary['date'] = date
    dictionary['type_of'] = type_of
    dictionary['currency'] = currency
    dictionary['value'] = value
    dictionary['from_where'] = from_where
    dictionary['to'] = to
    return dictionary
