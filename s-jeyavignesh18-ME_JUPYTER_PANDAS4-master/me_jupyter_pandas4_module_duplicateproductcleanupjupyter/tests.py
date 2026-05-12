import pandas as pd
from solution import clean_product_data  # Ensure solution.py has the implemented function

def test_remove_duplicates_and_filter_low_sales():
    """Test function with duplicate product names and low sales filtering."""
    test_data = pd.DataFrame({
        'Product': ['TV', 'Blender', 'Smartphone', 'TV', 'Book'],
        'Category': ['Furniture', 'Home', 'Furniture', 'Furniture', 'Electronics'],
        'Sales': [2079, 800, 2158, 2079, 500]
    })

    expected_data = pd.DataFrame({
        'Product': ['TV', 'Smartphone'],
        'Category': ['Furniture', 'Furniture'],
        'Sales': [2079, 2158]
    })

    result = clean_product_data(test_data, 1000)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data.reset_index(drop=True))

def test_empty_dataframe():
    """Test function with an empty DataFrame."""
    test_data = pd.DataFrame(columns=['Product', 'Category', 'Sales'])
    
    result = clean_product_data(test_data, 1000)
    assert result.empty  # Should return an empty DataFrame

test_remove_duplicates_and_filter_low_sales()
test_empty_dataframe()
print("✅ All tests passed.")
