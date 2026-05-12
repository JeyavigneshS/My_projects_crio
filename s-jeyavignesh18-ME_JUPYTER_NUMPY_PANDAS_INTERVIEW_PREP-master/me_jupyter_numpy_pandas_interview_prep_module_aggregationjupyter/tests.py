import pandas as pd
from solution import analyze_sales_data  # Make sure it's implemented in solution.py

def test_analyze_sales_data():
    """Test analyze_sales_data function using actual sales transaction data."""

    # Load dataset from URL
    url = "https://gitlab.crio.do/root/me_jupyter_numpy_pandas_interview_prep_datasets/-/raw/master/sales_transactions.csv"
    df = pd.read_csv(url)

    # Convert to list of dictionaries
    transactions = df.to_dict(orient="records")

    # Run the function
    result = analyze_sales_data(transactions)

    # Assertions on result structure
    assert isinstance(result, dict), "Function should return a dictionary"
    assert "total_sales_per_product" in result, "Missing key: total_sales_per_product"
    assert "top_3_products" in result, "Missing key: top_3_products"
    assert "unique_customer_count" in result, "Missing key: unique_customer_count"
    assert "filtered_transactions" in result, "Missing key: filtered_transactions"

    # Check types
    assert isinstance(result["total_sales_per_product"], dict), "total_sales_per_product should be a dict"
    assert isinstance(result["top_3_products"], list), "top_3_products should be a list"
    assert isinstance(result["unique_customer_count"], int), "unique_customer_count should be an int"
    assert isinstance(result["filtered_transactions"], list), "filtered_transactions should be a list"

    # Logical checks
    assert len(result["top_3_products"]) <= 3, "top_3_products should contain up to 3 items"
    assert result["unique_customer_count"] == df["Customer_ID"].nunique(), "Incorrect unique customer count"

    # Average sales check
    avg_sales = df["Sales"].mean()
    filtered_df = pd.DataFrame(result["filtered_transactions"])
    assert all(filtered_df["Sales"] > avg_sales), "filtered_transactions should only contain rows with sales above average"

    print("✅ Test Passed: analyze_sales_data() works correctly with the dataset.")
