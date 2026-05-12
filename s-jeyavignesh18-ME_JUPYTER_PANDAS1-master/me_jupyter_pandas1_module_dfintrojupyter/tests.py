import pandas as pd
from solution import create_product_dataframe, calculate_total_value

def test_create_product_dataframe():
    df = create_product_dataframe()
    assert not df.empty, "DataFrame is empty"
    assert list(df.columns) == ["Product", "Price", "Quantity"], "Column names mismatch"
    assert len(df) == 4, "Incorrect number of rows"
    print("\n✅ Test Passed: DataFrame created successfully.")
    print(df.head())

def test_calculate_total_value():
    df = create_product_dataframe()
    df = calculate_total_value(df)
    assert "Total Value" in df.columns, "Total Value column missing"
    assert all(df["Total Value"] == df["Price"] * df["Quantity"]), "Total Value calculation incorrect"
    print("\n✅ Test Passed: Total Value calculated successfully.")
    print(df)