import pandas as pd
import inspect
from solution import detect_missing_values

def test_detect_missing_values():
    """Test if missing values are correctly detected in a DataFrame."""
    # Check if df.isnull() is used in the function
    source_code = inspect.getsource(detect_missing_values)
    assert "isnull" in source_code, "df.isnull() is not used in the function"

    # Create a test DataFrame
    test_data = {'Customer': ['Alice', 'Bob', 'Charlie', 'David'],
                 'Total_Spend': [200.50, None, 150.75, None]}
    test_df = pd.DataFrame(test_data)

    # Get function results
    missing_values, missing_counts = detect_missing_values(test_df)

    # Check if output types are correct
    assert isinstance(missing_values, pd.DataFrame), "Missing values result should be a DataFrame"
    assert isinstance(missing_counts, pd.Series), "Missing counts result should be a Series"

    # Check if missing values are correctly detected
    assert missing_counts['Total_Spend'] == 2, "Missing values count for 'Total_Spend' is incorrect"

    print("✅ Test Passed: detect_missing_values() is implemented correctly.")