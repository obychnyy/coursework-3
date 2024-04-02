import json
from datetime import datetime


def load_operations():
    with open('../operations.json') as file:  # pragma: no cover
        return json.load(file)


def filtered(operation_list: list[dict]) -> list[dict]:
    """creates a list of dictionaries of only completed operations"""
    filtered_list = []
    for i in operation_list:
        if i and i['state'] == 'EXECUTED':
            filtered_list.append(i)
    return filtered_list


def sorter(filtered_list: list[dict]) -> list[dict]:
    """sorts the list by date from recent to oldes"""
    filtered_list.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return filtered_list


def cutter(filtered_list: list[dict]) -> list[dict]:
    """trims the list to the last 5 operations"""
    x = 0
    cut_list = []
    while x < 5:
        if len(filtered_list) < 5:
            return filtered_list
        else:
            cut_list.append(filtered_list[x])
            x += 1
    return cut_list


def data_structurer(dictionary: dict) -> str or None:
    """pulls values from the dictionary by keys and transfers them to variables"""
    date = dictionary["date"]
    type_of = dictionary["description"]
    currency = dictionary['operationAmount']['currency']['name']
    value = dictionary['operationAmount']['amount']
    from_where = dictionary.get('from')
    to = dictionary['to']
    return date, type_of, currency, value, from_where, to


def make_output_list(filtered_list: list[dict]) -> list[dict]:
    """processes data and collects dictionaries into a list"""
    output_list = []
    for i in filtered_list:
        date, type_of, currency, value, from_where, to = data_structurer(i)
        date = date_recycling(date)
        from_where = card_recycling(from_where)
        to = card_recycling(to)
        dictionary = make_output(date, type_of, currency, value, from_where, to)
        output_list.append(dictionary)
    return output_list


def date_recycling(date: str) -> str:
    """changes the date format from ISO to custom"""
    date = datetime.fromisoformat(date)
    return date.strftime('%d.%m.%Y')


def card_recycling(number: str) -> str:
    """masks the account or card number and breaks it into pieces of 4 characters"""
    card = []
    if number is not None:
        if number[-17] == ' ':
            card.extend([number[0:-17], ' ', number[-16:-12], ' ', number[-12:-10], '** **** ', number[-4:-1], number[len(number)-1]])
            number = ''.join(card)
        else:
            card.extend([number[0: -21], ' **', number[-4:-1], number[len(number)-1]])
            number = ''.join(card)
    return number


def make_output(date: str, type_of: str, currency: str, value: str, number_from: str or None, to: str) -> dict:
    """collects data into a dictionary"""
    dictionary = {'date': date, 'type_of': type_of, 'currency': currency, 'value': value, 'number_from': number_from,
                  'number_to': to}
    return dictionary
