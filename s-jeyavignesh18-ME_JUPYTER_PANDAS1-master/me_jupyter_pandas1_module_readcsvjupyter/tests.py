import pandas as pd
from solution import load_btc_market_price, load_btc_market_price_no_header, load_btc_market_price_with_names

def test_load_btc_market_price():
    """Test function for load_btc_market_price to verify correct data loading."""
    btc_data = load_btc_market_price()
    assert not btc_data.empty, "BTC market price data loading failed"
    print("✅ Test Passed: BTC market price data loaded successfully.")
    print(btc_data.head())

def test_load_btc_market_price_no_header():
    """Test function for load_btc_market_price_no_header to verify correct data loading."""
    btc_data = load_btc_market_price_no_header()
    assert not btc_data.empty, "BTC market price data loading failed (no header)"
    print("✅ Test Passed: BTC market price data (no header) loaded successfully.")
    print(btc_data.head())

def test_load_btc_market_price_with_names():
    """Test function for load_btc_market_price_with_names to verify correct data loading."""
    btc_data = load_btc_market_price_with_names()
    assert not btc_data.empty, "BTC market price data loading failed (with column names)"
    print("✅ Test Passed: BTC market price data (with column names) loaded successfully.")
    print(btc_data.head())