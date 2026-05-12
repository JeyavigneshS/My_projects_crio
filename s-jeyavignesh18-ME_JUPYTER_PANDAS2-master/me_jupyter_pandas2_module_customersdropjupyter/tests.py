import pandas as pd
import inspect
from solution import remove_customer_address_column

def test_remove_customer_address_column():
    """Test if the 'Customer Address' column is removed from the DataFrame."""
    # Check if df.drop() is used in the function
    source_code = inspect.getsource(remove_customer_address_column)
    assert "drop" in source_code, "df.drop() is not used in the function"

    # Check if the function returns a DataFrame without the 'Customer Address' column
    df = pd.DataFrame({
    "Customer Name": ["Alice", "Bob", "Charlie"],
    "Purchase Amount": [100, 250, 75],
    "Customer Address": ["123 St", "456 Ave", "789 Blvd"]
})
    result = remove_customer_address_column(df)
    assert isinstance(result, pd.DataFrame), "Function did not return a DataFrame"
    assert "Customer Address" not in result.columns, "'Customer Address' column was not removed"

    print("✅ Test Passed: remove_customer_address_column() is implemented correctly.")