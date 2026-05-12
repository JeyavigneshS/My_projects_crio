import pandas as pd
import inspect
from solution import create_country_dataframe, describe_country_dataframe

def test_create_country_dataframe():
    """Test if df.info() is called and a DataFrame is returned."""
    # Check if df.info() is used in the function
    source_code = inspect.getsource(create_country_dataframe)
    assert ".info()" in source_code, "df.info() is not called in the function"

    # Check if the function returns a DataFrame
    df = create_country_dataframe()
    assert isinstance(df, pd.DataFrame), "Function did not return a DataFrame"

    print("✅ Test Passed: create_country_dataframe() is implemented correctly.")

def test_describe_country_dataframe():
    """Test if df.describe() is called and a DataFrame is returned."""
    # Check if df.describe() is used in the function
    source_code = inspect.getsource(describe_country_dataframe)
    assert ".describe()" in source_code, "df.describe() is not called in the function"

    # Check if the function returns a DataFrame
    df = describe_country_dataframe()
    assert isinstance(df, pd.DataFrame), "Function did not return a DataFrame"

    print("✅ Test Passed: describe_country_dataframe() is implemented correctly.")