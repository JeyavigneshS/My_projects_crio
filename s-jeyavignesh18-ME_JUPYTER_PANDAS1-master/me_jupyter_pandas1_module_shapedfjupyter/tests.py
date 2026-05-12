import pandas as pd
import inspect
from solution import btc_market_price_shape

def test_btc_market_price_shape():
    """Test function to check the shape of the BTC market price DataFrame and its usage in the function."""
    df = btc_market_price_shape()

    # Check if df.shape is a tuple and has two elements
    assert isinstance(df.shape, tuple) and len(df.shape) == 2, f"Invalid shape: Expected (rows, columns), but found {df.shape}"

    # Check if 'df.shape' is actually used in the function
    source_code = inspect.getsource(btc_market_price_shape)
    assert ".shape" in source_code, "df.shape is not used in the function."

    print(f"✅ Test Passed: BTC market price DataFrame has a valid shape {df.shape} and 'df.shape' is used in the function.")
