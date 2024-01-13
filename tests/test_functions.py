import pytest
from main_code.functions import *


def test_sort_operation_list():
    assert (sort_operation_list([{"state": "EXECUTED", "date": "2018-12-20T16:43:26.929246"},
                                {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
                                {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
                                {"state": "EXECUTED", "date": "2018-07-11T02:26:18.671407"},
                                {"state": "EXECUTED", "date": "2018-04-04T17:33:34.701093"}]) ==
                                        [{'date': '2019-07-12T20:41:47.882230', 'state': 'EXECUTED'},
                                         {'date': '2018-12-20T16:43:26.929246', 'state': 'EXECUTED'},
                                         {'date': '2018-08-19T04:27:37.904916', 'state': 'EXECUTED'},
                                         {'date': '2018-07-11T02:26:18.671407', 'state': 'EXECUTED'},
                                         {'date': '2018-04-04T17:33:34.701093', 'state': 'EXECUTED'}])
    assert sort_operation_list([{}]) == []


def test_report_operation():
    assert sort_operation_list([{"state": "EXECUTED",
                                "date": "2019-07-12T20:41:47.882230",
                                "operationAmount": {
                                  "amount": "51463.70",
                                  "currency": {"name": "USD", "code": "USD"}
                                },
                                "description": "Перевод организации",
                                "from": "Счет 48894435694657014368",
                                "to": "Счет 38976430693692818358"
                              }]) == ['12.07.2019 Перевод организации '
                                      'Счет **4368 -> Счет **8358'
                                      '51463.70 USD']

    assert (sort_operation_list([{"state": "EXECUTED", 'date': '2019-07-12T20:41:47.882230'}]) ==
            [{'date': '2019-07-12T20:41:47.882230', 'state': 'EXECUTED'}])
    assert sort_operation_list([{"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230",
                                 'to': 'Счет 38976430693692818358'}]) == [{'date': '2019-07-12T20:41:47.882230',
                                                                           'state': 'EXECUTED',
                                                                           'to': 'Счет 38976430693692818358'}]
#