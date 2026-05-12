import pandas as pd
import inspect
from solution import drop_missing_contacts

def test_drop_missing_contacts():
    """Test if rows with missing 'Email' and 'Phone' are correctly removed from the DataFrame."""
    # Check if df.dropna() is used in the function
    source_code = inspect.getsource(drop_missing_contacts)
    assert "dropna" in source_code, "df.dropna() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'Customer Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Email': ['alice@example.com', None, 'charlie@example.com', None, 'eve@example.com', None, None],
        'Phone': ['1234567890', None, '9876543210', None, '1122334455', '9871234560', None]
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = drop_missing_contacts(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Check if the correct rows were removed
    expected_remaining_names = ['Alice', 'Charlie', 'Eve', 'Frank']
    assert list(result_df['Customer Name']) == expected_remaining_names, "Rows were not correctly removed"

    print("✅ Test Passed: drop_missing_contacts() is implemented correctly.")