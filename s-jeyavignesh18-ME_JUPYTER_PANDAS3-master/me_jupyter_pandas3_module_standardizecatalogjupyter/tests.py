import pandas as pd
import inspect
from solution import standardize_product_names

def test_standardize_product_names():
    """Test if product names are correctly standardized."""
    # Check if replace() is used in the function
    source_code = inspect.getsource(standardize_product_names)
    assert "replace" in source_code, "df.replace() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'Product ID': [101, 102, 103, 104, 105, 106],
        'Product Name': ['IPH 13', 'iPhone-13', 'Iphone 13', 'Samsung S10', 'S21-Samsung', 'IPHONE_13'],
        'Status': ['Active', 'Active', 'Active', 'Discontinued', 'Active', 'Active'],
        'Customer Feedback': ['Excellant phone', 'Greate quality', 'Good but battary issue', 'Poor durability', 'Amazing camera', 'Love the feautres']
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = standardize_product_names(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Expected standardized product names
    expected_product_names = ['iPhone 13', 'iPhone 13', 'iPhone 13', 'Samsung S10', 'Samsung S21', 'iPhone 13']

    # Check if product names are correctly standardized
    assert list(result_df['Product Name']) == expected_product_names, "Product names were not correctly standardized"

    print("\n✅ Test Passed: standardize_product_names() is implemented correctly.")