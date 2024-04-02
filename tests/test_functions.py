import pytest

from source import functions


def test_filtered():
    assert functions.filtered([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "CANCELED"}]) == ([{"state": "EXECUTED"}, {"state": "EXECUTED"}])
    assert functions.filtered([]) == []


def test_sorter():
    assert functions.sorter([{"date": "2018-03-23T10:45:06.972075"}, {"date": "2019-08-26T10:50:58.294041"}, {"date": "2018-06-30T02:08:58.425572"}]) == [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2018-06-30T02:08:58.425572"}, {"date": "2018-03-23T10:45:06.972075"}]


@pytest.mark.parametrize("list_of, cutted_list", [
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    (['', '', [], {}, 1], ['', '', [], {}, 1])
])
def test_cutter(list_of, cutted_list):
    assert functions.cutter(list_of) == (cutted_list)


def test_data_structurer():
    assert functions.data_structurer(
        {'date': 1, 'description': 2, 'operationAmount': {'currency': {'name': 3}, 'amount': 4}, 'from': 5,
         'to': 6}) == (1, 2, 3, 4, 5, 6)
    assert functions.data_structurer(
        {'date': 1, 'description': 2, 'operationAmount': {'currency': {'name': 3}, 'amount': 4},
         'to': 6}) == (1, 2, 3, 4, None, 6)


@pytest.mark.parametrize('date, result', [
    ("2019-08-26T10:50:58.294041", '26.08.2019'),
    ("2018-03-23T10:45:06.972075", '23.03.2018')
])
def test_date_recycling(date, result):
    assert functions.date_recycling(date) == result


@pytest.mark.parametrize('card_number, encrypted', [
    ('Счет 72082042523231456215', 'Счет **6215'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Maestro 3928549031574026', 'Maestro 3928 54** **** 4026')
])
def test_card_recycling(card_number, encrypted):
    assert functions.card_recycling(card_number) == (encrypted)


def test_make_output():
    assert functions.make_output('date', 'type_of', 'currency', 'value',
                                 'number_from', 'to') == {'date': 'date', 'type_of': 'type_of',
                                                          'currency': 'currency', 'value': 'value',
                                                          'number_from': 'number_from', 'number_to': 'to'}
    assert functions.make_output('date', 'type_of', 'currency', 'value',
                                 None, 'to') == {'date': 'date', 'type_of': 'type_of',
                                                          'currency': 'currency', 'value': 'value',
                                                          'number_from': None, 'number_to': 'to'}