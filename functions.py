import json

class operations:
    def __init__(self, date, from_where, to, amount, val):
        self.date = date
        self.from_where = from_where
        self.to = to
        self.amount = amount
        self.val = val


def load_operations():
    with open('operations.json') as file:
        operation_list = json.load(file)

    return operation_list
