import pytest
from src.wallet_withdrawal import withdraw


# Test 1: Normal withdrawal
def test_valid_withdrawal_returns_correct_balance():

    # Arrange
    wallet_balance = 1000
    wallet_amount = 400

    # Act
    withdrawn_balance = withdraw(wallet_balance, wallet_amount)

    # Assert
    assert withdrawn_balance == 600
    assert type(withdrawn_balance) is int


# Test 2: Withdrawing the entire balance
def test_withdraw_entire_balance_returns_zero():

    # Arrange
    wallet_balance = 1000
    wallet_amount = 1000

    # Act
    withdrawn_balance = withdraw(wallet_balance, wallet_amount)

    # Assert
    assert withdrawn_balance == 0
    assert type(withdrawn_balance) is int


# Test 3: Invalid withdrawal amounts
@pytest.mark.parametrize(
    "wallet_balance, wallet_amount",
    [
        (1000, 0),       # Zero withdrawal
        (1000, -100),    # Negative withdrawal
        (100, 200),      # Withdrawal exceeds balance
        (-100, 50),      # Negative balance
        (0, 0),          # Both values are zero
        (0, 100),        # Withdrawal with no balance
    ]
)
def test_invalid_withdrawal_raises_value_error(wallet_balance, wallet_amount):

    # Act and Assert
    with pytest.raises(ValueError):
        withdraw(wallet_balance, wallet_amount)


# Test 4: Invalid data types
@pytest.mark.parametrize(
    "wallet_balance, wallet_amount",
    [
        ("1000", 300),    # String balance
        (1000, "300"),    # String amount
        (1000.5, 300),   # Float balance
        (1000, 300.5),   # Float amount
        (True, 300),     # Boolean balance
        (1000, True),    # Boolean amount
        (False, 300),    # Boolean balance
        (1000, False),   # Boolean amount
        (None, 300),     # None balance
        (1000, None),    # None amount
    ]
)
def test_invalid_data_type_raises_type_error(wallet_balance, wallet_amount):

    # Act and Assert
    with pytest.raises(TypeError):
        withdraw(wallet_balance, wallet_amount)