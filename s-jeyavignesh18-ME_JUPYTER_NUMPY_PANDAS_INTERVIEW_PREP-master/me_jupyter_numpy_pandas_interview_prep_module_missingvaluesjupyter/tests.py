import pandas as pd
import inspect
from solution import clean_sales_data  # Make sure clean_sales_data is in solution.py

def test_clean_sales_data():
    """Test the clean_sales_data function using the provided dataset."""

    # Load dataset
    url = "https://gitlab.crio.do/root/me_jupyter_numpy_pandas_interview_prep_datasets/-/raw/master/sales_performance.csv"
    original_df = pd.read_csv(url)

    # Backup before mutation
    test_df = original_df.copy()

    # Get source code
    source_code = inspect.getsource(clean_sales_data)

    # Expected mean revenue before cleaning
    expected_mean = test_df['Revenue'].mean(skipna=True)

    # Count rows with missing Product
    rows_with_missing_product = test_df['Product'].isnull().sum()
    expected_row_count = len(test_df) - rows_with_missing_product

    # Apply cleaning
    cleaned_df = clean_sales_data(test_df)

    # Assertions
    assert isinstance(cleaned_df, pd.DataFrame), "Function should return a DataFrame"
    assert "fillna" in source_code, "fillna not used to handle missing Revenue"
    assert "replace" in source_code, "replace not used to handle Region values"
    assert "dropna" in source_code, "dropna not used to drop rows with missing Product"
    assert cleaned_df['Revenue'].isnull().sum() == 0, "Missing values in Revenue were not handled"
    assert round(expected_mean, 2) in cleaned_df['Revenue'].round(2).values, "Incorrect Revenue filling"
    assert 'Unknown' not in cleaned_df['Region'].values, "'Unknown' not replaced in Region"
    assert 'Not Specified' in cleaned_df['Region'].values, "'Not Specified' not found in Region"
    assert cleaned_df['Product'].isnull().sum() == 0, "Rows with missing Product were not dropped"
    assert len(cleaned_df) == expected_row_count, "Unexpected number of rows after cleaning"
