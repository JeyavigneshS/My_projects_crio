import pandas as pd
import inspect
from solution import sort_dataframe

def test_sort_dataframe():
    """Test if the DataFrame is correctly sorted by different criteria."""
    # Check if sort_values() is used in the function
    source_code = inspect.getsource(sort_dataframe)
    assert "sort_values" in source_code, "sort_values() is not used in the function"

    # Create test DataFrame
    df = pd.DataFrame({
        "Customer Name": ["Alice", "Bob", "Charlie", "David"],
        "Purchase Amount": [250, 100, 75, 150],
        "Customer Type": ["Regular", "VIP", "Regular", "VIP"]
    })

    # Apply function
    sorted_amount, sorted_name, sorted_type_amount = sort_dataframe(df)

    # Validate DataFrame structure
    assert isinstance(sorted_amount, pd.DataFrame), "Function did not return a DataFrame for sorting by amount"
    assert isinstance(sorted_name, pd.DataFrame), "Function did not return a DataFrame for sorting by name"
    assert isinstance(sorted_type_amount, pd.DataFrame), "Function did not return a DataFrame for sorting by type and amount"

    # Validate sorting order
    expected_order_amount = df.sort_values("Purchase Amount", ascending=False)["Customer Name"].tolist()
    expected_order_name = df.sort_values("Customer Name")["Customer Name"].tolist()
    expected_order_type_amount = df.sort_values(["Customer Type", "Purchase Amount"], ascending=[True, False])["Customer Name"].tolist()

    assert list(sorted_amount["Customer Name"]) == expected_order_amount, "Sorting by amount is incorrect"
    assert list(sorted_name["Customer Name"]) == expected_order_name, "Sorting by name is incorrect"
    assert list(sorted_type_amount["Customer Name"]) == expected_order_type_amount, "Sorting by type and amount is incorrect"

    print("✅ Test Passed: sort_dataframe() is implemented correctly.")