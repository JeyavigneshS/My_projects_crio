import pandas as pd
from solution import create_marvel_dataframe

def test_create_marvel_dataframe():
    """Test function for create_marvel_dataframe to verify correct DataFrame creation."""
    df = create_marvel_dataframe()

    # Ensure DataFrame is not empty
    assert not df.empty, "Marvel DataFrame creation failed (empty DataFrame)"

    # Ensure shape is correct (10 rows, 3 columns)
    expected_shape = (10, 3)
    assert df.shape == expected_shape, f"Shape mismatch: Expected {expected_shape}, but found {df.shape}"

    print(f"✅ Test Passed: Marvel DataFrame created successfully with shape {df.shape}.")
    print(df)