import pandas as pd
import inspect
from solution import fill_missing_property_prices

def test_fill_missing_property_prices():
    """Test if missing 'Price ($)' values are correctly filled with the mean property price."""
    # Check if fillna() is used in the function
    source_code = inspect.getsource(fill_missing_property_prices)
    assert "fillna" in source_code, "df.fillna() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'Property ID': [101, 102, 103, 104, 105, 106, 107],
        'Location': ['Downtown', 'Suburbs', 'Downtown', 'Suburbs', 'City Center', 'Downtown', 'Suburbs'],
        'Price ($)': [500000, None, 550000, 470000, None, 530000, None]
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = fill_missing_property_prices(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Compute expected mean
    expected_mean = test_df['Price ($)'].mean(skipna=True)
    expected_filled_values = test_df['Price ($)'].fillna(expected_mean).tolist()

    # Check if missing values are correctly filled
    assert list(result_df['Price ($)']) == expected_filled_values, "Missing prices were not correctly filled"

    print("\n✅ Test Passed: fill_missing_property_prices() is implemented correctly.")