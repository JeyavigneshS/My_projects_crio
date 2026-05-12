import pandas as pd
from solution import analyze_sales  # Ensure solution.py contains the implemented function

def test_analyze_sales():
    """Test function with multiple categories and products."""
    test_data = pd.DataFrame({
        'Product': ['TV', 'Blender', 'Smartphone', 'Book'],
        'Category': ['Furniture', 'Home', 'Furniture', 'Electronics'],
        'Sales': [2079, 3551, 2158, 3948]
    })

    expected_output = {
        'Furniture': {'sum': 4237, 'mean': 2118.5, 'count': 2},
        'Home': {'sum': 3551, 'mean': 3551.0, 'count': 1},
        'Electronics': {'sum': 3948, 'mean': 3948.0, 'count': 1}
    }

    result = analyze_sales(test_data)
    assert result == expected_output

def test_empty_dataframe():
    """Test function with an empty dataframe."""
    test_data = pd.DataFrame(columns=['Product', 'Category', 'Sales'])
    
    result = analyze_sales(test_data)
    assert result == {}

def test_single_category():
    """Test function when all products belong to one category."""
    test_data = pd.DataFrame({
        'Product': ['TV', 'Laptop', 'Sofa'],
        'Category': ['Furniture', 'Furniture', 'Furniture'],
        'Sales': [2000, 3000, 2500]
    })

    expected_output = {
        'Furniture': {'sum': 7500, 'mean': 2500.0, 'count': 3}
    }

    result = analyze_sales(test_data)
    assert result == expected_output

test_analyze_sales()
test_empty_dataframe()
test_single_category()
print("✅ All tests passed.")
