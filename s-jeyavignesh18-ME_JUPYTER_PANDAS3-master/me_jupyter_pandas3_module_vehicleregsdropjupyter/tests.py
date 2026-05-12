import pandas as pd
import inspect
from solution import drop_missing_vehicle_data

def test_drop_missing_vehicle_data():
    """Test if rows with missing 'License Plate' and 'Registration Date' are correctly removed from the DataFrame."""
    # Check if df.dropna() is used in the function
    source_code = inspect.getsource(drop_missing_vehicle_data)
    assert "dropna" in source_code, "df.dropna() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'Owner Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'License Plate': ['ABC123', None, 'XYZ987', None, 'LMN456', None, None],
        'Registration Date': ['2023-05-10', None, '2022-11-23', None, '2021-09-15', '2020-07-30', None]
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = drop_missing_vehicle_data(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Check if the correct rows were removed
    expected_remaining_names = ['Alice', 'Charlie', 'Eve', 'Frank']
    assert list(result_df['Owner Name']) == expected_remaining_names, "Rows were not correctly removed"

    print("✅ Test Passed: drop_missing_vehicle_data() is implemented correctly.")