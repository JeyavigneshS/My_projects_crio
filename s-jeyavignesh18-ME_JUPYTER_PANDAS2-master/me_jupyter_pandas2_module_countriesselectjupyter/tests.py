import pandas as pd
import inspect
from solution import select_country_data, filter_country_data

def test_select_country_data():
    """Test if df.iloc is used in the function and returns expected length of values."""
    # Check if df.iloc is used in the function
    source_code = inspect.getsource(select_country_data)
    assert "iloc" in source_code, "df.iloc is not used in the function"

    # Check if the function returns expected number of values
    results = select_country_data()
    assert isinstance(results, tuple), "Function did not return a tuple"
    assert len(results) == 4, "Function did not return the expected number of values"

    print("✅ Test Passed: select_country_data() is implemented correctly.")

def test_filter_country_data():
    """Test if df.loc is used in the function and returns a Series."""
    # Check if df.loc is used in the function
    source_code = inspect.getsource(filter_country_data)
    assert "loc" in source_code, "df.loc is not used in the function"

    # Check if the function returns a Pandas Series
    result = filter_country_data()
    assert isinstance(result, pd.Series), "Function did not return a Pandas Series"

    print("✅ Test Passed: filter_country_data() is implemented correctly.")