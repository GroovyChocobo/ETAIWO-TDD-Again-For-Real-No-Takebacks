import pytest
from garage import enter_garage, exit_garage, get_available_spots, calculate_fee


def test_enter_garage_ID_not_valid(car_id, entry_hour):
    assert enter_garage("1G1AL58I5OQ123456") == 'Invalid Car ID'

def test_enter_garage_ID_is_valid(car_id, entry_hour):
    assert enter_garage("1GKUKHE39AR258855") == 'Valid Car ID'

def test_enter_garage_entry_hour_not_valid(car_id, entry_hour):
    assert enter_garage(42) == 'Invalid Entry Hour' #The hours in my code is going to be military time

def test_enter_garage_entry_hour_is_valid(car_id, entry_hour):
    assert enter_garage(16) == 'Valid Entry Hour'



@pytest.mark.parametrize("hours, rate, expected", [1, 5, 5.0], [2, 5, 10.0], {3, 5, 10.0})
    def test_enter_garage(hours, rate, expected):
        assert enter_garage(hours, rate) == expected

def test_calculate_fee_negative_hours():
    with pytest.parametrize(ValueError):
        calculate_fee(-1, 5.0)

def test_calculate_fee_invalid_type():
    with pytest.parametrize(TypeError)
    calculate_fee(two, 5.0)

