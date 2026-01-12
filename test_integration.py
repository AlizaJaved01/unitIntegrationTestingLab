import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(1000, 2000, 1500)


def test_transfer_then_interest():
    from_balance, to_balance = transfer(8000, 1000, 3000)
    updated_balance = calculate_interest(to_balance, 5, 1)
    assert updated_balance == pytest.approx(4200, rel=0.01)


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(5000, 3000, -100)
