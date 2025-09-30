# exercise 1
import pytest
import datetime


def add_numbers(first_num, second_num):
    return first_num + second_num


@pytest.fixture(scope="function")
def current_datetime():
    return datetime.datetime.now(datetime.UTC)


def test_add_numbers(current_datetime):
    print(current_datetime)
    result = add_numbers(1, 2)
    assert result == 3
