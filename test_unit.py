import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


def test_deposit():
	assert deposit(1000, 500) == 1500


def test_deposit_invalid():
	with pytest.raises(ValueError):
		deposit(1000, -100)


def test_withdraw():
	assert withdraw(1000, 200) == 800


def test_withdraw_invalid():
	with pytest.raises(ValueError):
		withdraw(500, 1000)


def test_interest():
	assert calculate_interest(1000, 10, 1) == 1100


def test_loan_eligible():
	assert check_loan_eligibility(6000, 750) is True
