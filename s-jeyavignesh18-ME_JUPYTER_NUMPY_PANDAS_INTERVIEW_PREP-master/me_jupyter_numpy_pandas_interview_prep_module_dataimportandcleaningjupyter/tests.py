import pandas as pd
import inspect
from solution import clean_customer_data  # Ensure it's implemented in solution.py

def test_clean_customer_data():
    """Test clean_customer_data function with actual customer dataset."""

    # Dataset URL
    file_path = "https://gitlab.crio.do/root/me_jupyter_numpy_pandas_interview_prep_datasets/-/raw/master/customer_data.csv"

    # Call the function
    cleaned_df = clean_customer_data(file_path)

    # Check returned type
    assert isinstance(cleaned_df, pd.DataFrame), "Function should return a DataFrame"

    # Check column name formatting
    for col in cleaned_df.columns:
        assert col == col.lower(), "Column names should be lowercase"
        assert " " not in col, "Column names should not contain spaces"
        assert isinstance(col, str), "Column names should be strings"

    # Check for duplicates
    assert cleaned_df.duplicated().sum() == 0, "Duplicate rows were not removed"

    # Check for datetime conversion
    if 'date_of_purchase' in cleaned_df.columns:
        assert pd.api.types.is_datetime64_any_dtype(cleaned_df['date_of_purchase']), "'date_of_purchase' column is not datetime"

    print("✅ Test Passed: clean_customer_data() works correctly with the dataset.")
