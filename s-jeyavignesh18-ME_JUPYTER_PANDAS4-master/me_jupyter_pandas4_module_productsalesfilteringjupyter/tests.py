import pandas as pd
from solution import filter_and_sort_products

def test_standard_case():
    data = {
        'Product': ['TV', 'Laptop', 'Phone', 'Headphones', 'Speaker'],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Home'],
        'Sales': [2000, 3000, 500, 1200, 2500]
    }
    df = pd.DataFrame(data)

    df_filtered_sorted = filter_and_sort_products(df)

    assert not df_filtered_sorted.empty, "Filtered DataFrame should not be empty"

    assert all(df_filtered_sorted['Sales'] > 1000), "All products should have sales > 1000"

    assert all(df_filtered_sorted['Category'] == 'Electronics'), "All products should be in 'Electronics' category"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Product', 'Category', 'Sales'])
    df_filtered_sorted = filter_and_sort_products(df)
    assert df_filtered_sorted.empty, "Expected an empty DataFrame"

def test_no_qualifying_products():
    data = {
        'Product': ['A', 'B', 'C'],
        'Category': ['Electronics', 'Home', 'Electronics'],
        'Sales': [500, 800, 900]
    }
    df = pd.DataFrame(data)

    df_filtered_sorted = filter_and_sort_products(df)

    assert df_filtered_sorted.empty, "Expected an empty DataFrame when no products qualify"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_no_qualifying_products()
    print("All tests passed!")
