import pytest
from garage import enter_garage


def test_enter_garage_ID_not_valid(car_id, entry_hour):
    assert enter_garage("1G1AL58I5OQ123456") == 'Invalid Car ID'