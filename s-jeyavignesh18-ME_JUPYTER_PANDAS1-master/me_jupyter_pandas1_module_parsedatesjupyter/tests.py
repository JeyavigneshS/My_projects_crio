import pandas as pd
from solution import load_btc_market_price_with_parsed_dates

def test_load_btc_market_price_with_parsed_dates():
    """Test function for load_btc_market_price_with_parsed_dates to verify date parsing."""
    df = load_btc_market_price_with_parsed_dates()

    # Ensure DataFrame is not empty
    assert not df.empty, "BTC market price data loading failed (empty DataFrame)"

    # Ensure 'Timestamp' column exists
    assert 'Timestamp' in df.columns, "Missing 'Timestamp' column"

    # Ensure 'Timestamp' column is of datetime type
    assert pd.api.types.is_datetime64_any_dtype(df['Timestamp']), f"'Timestamp' column is not datetime type: {df['Timestamp'].dtype}"

    print("✅ Test Passed: BTC market price data loaded successfully with parsed dates.")
    print(df.head())
    print("🔍 Data Types:")
    print(df.dtypes)
