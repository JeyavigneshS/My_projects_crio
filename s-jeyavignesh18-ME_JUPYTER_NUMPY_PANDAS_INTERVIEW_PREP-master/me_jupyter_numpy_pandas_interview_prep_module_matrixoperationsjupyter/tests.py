import numpy as np
import inspect
from solution import analyze_sales_data  # Ensure the function is defined in solution.py

def test_analyze_sales_data():
    """Test the analyze_sales_data function with actual dataset."""

    # Load dataset from URL
    df = pd.read_csv(url)

    # Drop non-numeric columns (like "Product") and convert to NumPy array
    sales_data = df.select_dtypes(include=[float, int]).to_numpy()

    # Run analysis
    result = analyze_sales_data(sales_data)

    # Extract outputs
    total_revenue = result["total_revenue"]
    mean_revenue = result["mean_revenue"]
    discounted_sales = result["discounted_sales"]
    highest_avg_index = result["highest_average_product_index"]

    # Check result types
    assert isinstance(total_revenue, np.ndarray), "total_revenue should be a NumPy array"
    assert isinstance(mean_revenue, float) or isinstance(mean_revenue, np.floating), "mean_revenue should be a float"
    assert isinstance(discounted_sales, np.ndarray), "discounted_sales should be a NumPy array"
    assert isinstance(highest_avg_index, int), "highest_average_product_index should be an integer"

    # Check values
    assert not np.isnan(total_revenue).any(), "total_revenue should not contain NaN"
    assert not np.isnan(mean_revenue), "mean_revenue should not be NaN"
    assert np.all(discounted_sales[sales_data <= 5000] == sales_data[sales_data <= 5000]), "Values ≤ 5000 should not be discounted"
    assert np.all(discounted_sales[sales_data > 5000] == sales_data[sales_data > 5000] * 0.9), "Values > 5000 should be discounted"

    # Check product index is within bounds
    assert 0 <= highest_avg_index < sales_data.shape[1], "highest_average_product_index out of bounds"

    print("✅ Test Passed: analyze_sales_data() works correctly on the provided dataset.")