from source import functions

def test_filtered():
    assert functions.filtered([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "CANCELED"}]) == ([{"state": "EXECUTED"}, {"state": "EXECUTED"}])
    assert functions.filtered([]) == []


def test_sorter():
    assert functions.sorter([{"date": "2018-03-23T10:45:06.972075"}, {"date": "2019-08-26T10:50:58.294041"}, {"date": "2018-06-30T02:08:58.425572"}]) == [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2018-06-30T02:08:58.425572"}, {"date": "2018-03-23T10:45:06.972075"}]


def