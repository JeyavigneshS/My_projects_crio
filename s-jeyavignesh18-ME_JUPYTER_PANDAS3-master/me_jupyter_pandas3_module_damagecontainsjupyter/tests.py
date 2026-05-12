import pandas as pd
import inspect
from solution import extract_product_issues

def test_extract_product_issues():
    """Test if reviews mentioning missing or damaged products are correctly extracted."""
    # Check if str.contains() is used in the function
    source_code = inspect.getsource(extract_product_issues)
    assert "str.contains" in source_code, "str.contains() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'Review ID': [101, 102, 103, 104, 105, 106],
        'Customer Review': [
            'The delivery was late, very disappointed!',
            'Great product, arrived on time.',
            'I love the phone but the charger was missing.',
            'Delivery took longer than expected, not happy.',
            'Excellent quality, highly recommend it!',
            'The package was damaged upon arrival.'
        ]
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = extract_product_issues(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Expected extracted reviews
    expected_reviews = [
        'I love the phone but the charger was missing.',
        'The package was damaged upon arrival.'
    ]

    # Check if the correct reviews were extracted
    assert list(result_df['Customer Review']) == expected_reviews, "Reviews mentioning product issues were not correctly extracted"

    print("✅ Test Passed: extract_product_issues() is implemented correctly.")