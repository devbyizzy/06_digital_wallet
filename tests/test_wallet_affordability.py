import pytest
from src.wallet_affordability import can_afford


# Test 1: Valid purchase amounts
@pytest.mark.parametrize(
    "wallet_balance, item_price, expected",
    [
        (1000, 500, True),    # Enough money
        (300, 500, False),    # Not enough money
        (500, 500, True),     # Exact amount
        (500, 0, True),       # Free purchase
        (0, 0, True),         # Both values are zero
        (0, 100, False),      # Zero balance
    ]
)
def test_purchase_affordability(wallet_balance, item_price, expected):

    # Arrange
    # Test data is prepared using parametrize

    # Act
    purchase_result = can_afford(wallet_balance, item_price)

    # Assert
    assert purchase_result is expected


# Test 2: Invalid purchase values
@pytest.mark.parametrize(
    "wallet_balance, item_price",
    [
        (-100, 200),     # Negative balance
        (500, -100),     # Negative price
        (-100, -100),    # Both values are negative
        (-100, 0),       # Negative balance with zero price
    ]
)
def test_invalid_purchase_raises_value_error(wallet_balance, item_price):

    # Act and Assert
    with pytest.raises(ValueError):
        can_afford(wallet_balance, item_price)


# Test 3: Invalid data types
@pytest.mark.parametrize(
    "wallet_balance, item_price",
    [
        ("1000", 500),   # String balance
        (1000, "500"),   # String price
        (1000.5, 500),  # Float balance
        (1000, 500.5),  # Float price
        (True, 500),    # Boolean balance
        (1000, True),   # Boolean price
        (False, 500),   # Boolean balance
        (1000, False),  # Boolean price
        (None, 500),    # None balance
        (1000, None),   # None price
    ]
)
def test_invalid_data_type_raises_type_error(wallet_balance, item_price):

    # Act and Assert
    with pytest.raises(TypeError):
        can_afford(wallet_balance, item_price)