import pytest
from main_code.main import *


def test_operation_show():
    assert operation_show([{"id": 407169720, "state": "EXECUTED",
    "date": "2018-02-03T14:52:08.093722",
    "operationAmount": {"amount": "67011.26", "currency": {
        "name": "руб.", "code": "RUB"}},
    "description": "Перевод с карты на карту",
    "from": "MasterCard 4047671689373225",
    "to": "Maestro 3806652527413662"
    }]) == ('05.11.2019 Открытие вклада Счет **8381 -> Счет **8381 41096.24USD')