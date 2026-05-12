import pandas as pd
import inspect
from solution import create_sample_dataframe, create_and_analyze_dataframe

def test_create_sample_dataframe():
    """Test function for create_sample_dataframe to verify correct data creation and df.dtypes usage."""
    df = create_sample_dataframe()
    assert not df.empty, "DataFrame creation failed (empty DataFrame)"
    function_source = inspect.getsource(create_sample_dataframe)
    assert "df.dtypes" in function_source, "df.dtypes is not used in the function"
    print("✅ Test Passed: Sample DataFrame created successfully and `df.dtypes` is used.")
    print(df)
    print("🔍 Data Types:")
    print(df.dtypes)

def test_create_and_analyze_dataframe():
    """Test function for create_and_analyze_dataframe to verify correct data creation, type conversion, and average age calculation."""
    df, avg_age = create_and_analyze_dataframe()
    assert not df.empty, "DataFrame creation failed (empty DataFrame)"
    assert df["Age"].dtype == 'int64', f"Data type mismatch: 'Age' should be int, but found {df['Age'].dtype}"
    expected_avg_age = (25 + 30 + 35) / 3
    assert avg_age == expected_avg_age, f"Incorrect average age: Expected {expected_avg_age}, but found {avg_age}"
    function_source = inspect.getsource(create_and_analyze_dataframe)
    assert ".astype(int)" in function_source, "astype(int) is not used in the function"
    assert ".mean()" in function_source, "mean() is not used in the function"
    print(f"✅ Test Passed: DataFrame created successfully, 'Age' converted to int, and average age calculated correctly ({avg_age}).")
    print(df)
    print("🔍 Data Types:")
    print(df.dtypes)