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


def test_date_operation():
    assert date_operation([{"date": "2018-12-28T23:10:35.459698"}]) == '28.12.2018'


def test_mask_score_number():
    assert mask_score_number([{"to": "Счет 96231448929365202391"}]) == 'Счет **2391'


def test_mask_card_number():
    assert test_mask_score_number([{"from": "MasterCard 4047671689373225"}]) == 'MasterCard 4047 67** **** 3225'
