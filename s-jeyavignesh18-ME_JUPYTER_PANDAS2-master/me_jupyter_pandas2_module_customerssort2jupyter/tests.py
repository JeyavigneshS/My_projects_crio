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
        "Customer Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
        "Purchase Amount": [120, 250, 75, 300, 150, 200, 100],
        "City": ["New York", "Los Angeles", "Chicago", "Houston", "New York", "Chicago", "Los Angeles"],
        "Purchase Date": ["2024-03-10", "2024-02-20", "2024-01-15", "2024-03-05", "2024-02-28", "2024-01-10", "2024-02-25"]
    })

    df["Purchase Date"] = pd.to_datetime(df["Purchase Date"])

    # Apply function
    sorted_amount, sorted_name, sorted_city_amount, sorted_date = sort_dataframe(df)

    # Validate DataFrame structure
    assert isinstance(sorted_amount, pd.DataFrame), "Function did not return a DataFrame for sorting by amount"
    assert isinstance(sorted_name, pd.DataFrame), "Function did not return a DataFrame for sorting by name"
    assert isinstance(sorted_city_amount, pd.DataFrame), "Function did not return a DataFrame for sorting by city and amount"
    assert isinstance(sorted_date, pd.DataFrame), "Function did not return a DataFrame for sorting by date"

    # Validate sorting order
    expected_order_amount = df.sort_values("Purchase Amount", ascending=False)["Customer Name"].tolist()
    expected_order_name = df.sort_values("Customer Name")["Customer Name"].tolist()
    expected_order_city_amount = df.sort_values(["City", "Purchase Amount"], ascending=[True, False])["Customer Name"].tolist()
    expected_order_date = df.sort_values("Purchase Date")["Customer Name"].tolist()

    assert list(sorted_amount["Customer Name"]) == expected_order_amount, "Sorting by amount is incorrect"
    assert list(sorted_name["Customer Name"]) == expected_order_name, "Sorting by name is incorrect"
    assert list(sorted_city_amount["Customer Name"]) == expected_order_city_amount, "Sorting by city and amount is incorrect"
    assert list(sorted_date["Customer Name"]) == expected_order_date, "Sorting by date is incorrect"

    print("✅ Test Passed: sort_dataframe() is implemented correctly.")