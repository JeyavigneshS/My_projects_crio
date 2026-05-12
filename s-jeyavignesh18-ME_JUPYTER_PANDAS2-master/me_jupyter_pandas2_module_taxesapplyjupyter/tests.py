import pandas as pd
import inspect

def test_apply_total_price_tax():
    """Test if the 'Total Price (After Tax)' column is correctly added and calculated."""
    # Check if apply() is used in the function
    source_code = inspect.getsource(apply_total_price_tax)
    assert "apply" in source_code, "apply() is not used in the function"

    # Create test DataFrame
    df = pd.DataFrame({
        "Customer Name": ["Alice", "Bob", "Charlie", "David"],
        "Purchase Amount": [250, 100, 75, 150]
    })

    # Apply function
    result = apply_total_price_tax(df)

    # Validate DataFrame structure
    assert isinstance(result, pd.DataFrame), "Function did not return a DataFrame"
    assert "Total Price (After Tax)" in result.columns, "'Total Price (After Tax)' column was not added"

    # Validate tax calculation
    expected_prices = [287.5, 110.0, 78.75, 165.0]
    assert list(result["Total Price (After Tax)"]) == expected_prices, "Total prices were not calculated correctly"

    print("✅ Test Passed: apply_total_price_tax() is implemented correctly.")