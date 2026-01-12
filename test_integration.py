import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
	b1, b2 = transfer(5000, 2000, 1000)
	assert b1 == 4000
	assert b2 == 3000


def test_transfer_fail():
	with pytest.raises(ValueError):
		transfer(500, 2000, 1000)


def test_transfer_with_interest():
	b1, b2 = transfer(10000, 5000, 2000)
	result = calculate_interest(b2, 10, 1)
	assert round(result, 2) == 7700

