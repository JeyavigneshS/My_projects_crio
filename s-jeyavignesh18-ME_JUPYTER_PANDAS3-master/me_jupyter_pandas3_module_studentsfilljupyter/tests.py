import pandas as pd
import inspect
from solution import fill_missing_marks

def test_fill_missing_marks():
    """Test if missing 'Total Marks' values are correctly filled with the mean of available marks."""
    # Check if fillna() is used in the function
    source_code = inspect.getsource(fill_missing_marks)
    assert "fillna" in source_code, "df.fillna() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Total Marks': [85, None, 90, 78, None, 92, None]
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = fill_missing_marks(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Compute expected mean
    expected_mean = test_df['Total Marks'].mean(skipna=True)
    expected_filled_values = test_df['Total Marks'].fillna(expected_mean).tolist()

    # Check if missing values are correctly filled
    assert list(result_df['Total Marks']) == expected_filled_values, "Missing marks were not correctly filled"

    print("\n✅ Test Passed: fill_missing_marks() is implemented correctly.")