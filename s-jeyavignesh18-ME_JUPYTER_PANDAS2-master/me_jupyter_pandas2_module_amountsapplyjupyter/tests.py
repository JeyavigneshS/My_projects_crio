import pandas as pd
import inspect
from solution import apply_purchase_category

def test_apply_purchase_category():
    """Test if the 'Purchase Category' column is correctly added and categorized."""
    # Check if apply() is used in the function
    source_code = inspect.getsource(apply_purchase_category)
    assert "apply" in source_code, "apply() is not used in the function"

    # Create test DataFrame
    df = pd.DataFrame({
        "Customer Name": ["Alice", "Bob", "Charlie", "David"],
        "Purchase Amount": [100, 250, 75, 150]
    })

    # Apply function
    result = apply_purchase_category(df)

    # Validate DataFrame structure
    assert isinstance(result, pd.DataFrame), "Function did not return a DataFrame"
    assert "Purchase Category" in result.columns, "'Purchase Category' column was not added"

    # Validate category assignment
    expected_categories = ["Medium", "High", "Low", "Medium"]
    assert list(result["Purchase Category"]) == expected_categories, "Purchase categories were not assigned correctly"

    print("✅ Test Passed: apply_purchase_category() is implemented correctly.")