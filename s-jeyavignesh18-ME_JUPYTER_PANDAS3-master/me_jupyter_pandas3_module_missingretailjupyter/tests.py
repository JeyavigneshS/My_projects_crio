import pandas as pd
import inspect
from solution import detect_missing_values

def test_detect_missing_values():
    """Test if missing values are correctly detected in a DataFrame."""
    # Check if df.isnull() is used in the function
    source_code = inspect.getsource(detect_missing_values)
    assert "isnull" in source_code, "df.isnull() is not used in the function"

    # Create a test DataFrame
    test_data = {
        "Customer ID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", None, "David", "Eve"],
        "Age": [25, None, 30, 40, 35],
        "Total Spend ($)": [200.50, None, 150.75, None, 180.00],
        "City": ["New York", "Los Angeles", "Chicago", None, "Houston"]
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    missing_values, missing_counts = detect_missing_values(test_df)

    # Check if output types are correct
    assert isinstance(missing_values, pd.DataFrame), "Missing values result should be a DataFrame"
    assert isinstance(missing_counts, pd.Series), "Missing counts result should be a Series"

    # Check if missing values are correctly detected
    expected_missing_counts = {
        "Customer ID": 0,
        "Name": 1,
        "Age": 1,
        "Total Spend ($)": 2,
        "City": 1
    }

    for column, expected_count in expected_missing_counts.items():
        assert missing_counts[column] == expected_count, f"Missing values count for '{column}' is incorrect"

    print("✅ Test Passed: detect_missing_values() is implemented correctly.")