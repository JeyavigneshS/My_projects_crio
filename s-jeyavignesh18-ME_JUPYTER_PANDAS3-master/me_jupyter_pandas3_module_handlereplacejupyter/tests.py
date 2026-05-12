import pandas as pd
import inspect
from solution import update_social_media_handles

def test_update_social_media_handles():
    """Test if social media handles are correctly updated."""
    # Check if replace() is used in the function
    source_code = inspect.getsource(update_social_media_handles)
    assert "replace" in source_code, "df.replace() is not used in the function"

    # Create a test DataFrame
    test_data = {
        'User ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'User Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
        'Social Media Handle': ['@alice123', '@bob_1990', '@charlie_doe', '@david_x', '@eve_new', '@frank007', '@grace_22', '@henry_blog', '@ivy_artist', '@jack_sport']
    }
    test_df = pd.DataFrame(test_data)

    # Get function results
    result_df = update_social_media_handles(test_df)

    # Check if the function returns a DataFrame
    assert isinstance(result_df, pd.DataFrame), "Function did not return a DataFrame"

    # Expected updated social media handles
    expected_handles = ['@alice_official', '@bob_worldwide', '@charlie_real', '@david_x', '@eve_official', '@frank_global', '@grace_22', '@henry_blog', '@ivy_artist', '@jack_sport']

    # Check if social media handles are correctly updated
    assert list(result_df['Social Media Handle']) == expected_handles, "Social media handles were not correctly updated"

    print("\n✅ Test Passed: update_social_media_handles() is implemented correctly.")