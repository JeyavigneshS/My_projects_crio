import pandas as pd
import inspect
from solution import select_dataframe_values, filter_customers_by_city

def test_select_dataframe_values():
    """Test if df.iloc is used in the function and returns expected values."""
    # Check if df.iloc is used in the function
    source_code = inspect.getsource(select_dataframe_values)
    assert "iloc" in source_code, "df.iloc is not used in the function"

    # Check if the function returns expected values
    results = select_dataframe_values()
    assert isinstance(results, tuple), "Function did not return a tuple of values"
    assert len(results) == 4, "Function did not return the expected number of values"

    print("✅ Test Passed: select_dataframe_values() is implemented correctly.")

def test_filter_customers_by_city():
    """Test if df.loc is used in the function and returns a DataFrame."""
    # Check if df.loc is used in the function
    source_code = inspect.getsource(filter_customers_by_city)
    assert "loc" in source_code, "df.loc is not used in the function"

    # Check if the function returns a DataFrame
    result = filter_customers_by_city()
    assert isinstance(result, pd.DataFrame), "Function did not return a DataFrame"

    print("✅ Test Passed: filter_customers_by_city() is implemented correctly.")