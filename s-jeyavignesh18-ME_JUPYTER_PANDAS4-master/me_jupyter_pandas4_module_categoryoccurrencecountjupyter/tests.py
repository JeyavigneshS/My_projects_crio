import pandas as pd
from solution import analyze_product_categories

def test_standard_case():
    data = {
        'Product': ['TV', 'Blender', 'Smartphone', 'Book', 'Laptop', 'Chair'],
        'Category': ['Electronics', 'Home', 'Electronics', 'Books', 'Electronics', 'Furniture']
    }
    df = pd.DataFrame(data)

    unique_categories, df_category_counts = analyze_product_categories(df)

    assert 'Category' in df_category_counts.columns, "Expected 'Category' column"

    assert 'Count' in df_category_counts.columns, "Expected 'Count' column"

    assert len(unique_categories) == 4, "Expected 4 unique categories"

    assert df_category_counts[df_category_counts['Category'] == 'Electronics']['Count'].values[0] == 3, "Expected 3 products in 'Electronics' category"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Product', 'Category'])
    unique_categories, df_category_counts = analyze_product_categories(df)
    assert unique_categories == [], "Expected an empty list of categories"
    assert df_category_counts.empty, "Expected an empty DataFrame"

def test_single_category():
    data = {'Product': ['Item1', 'Item2', 'Item3'], 'Category': ['Electronics', 'Electronics', 'Electronics']}
    df = pd.DataFrame(data)

    unique_categories, df_category_counts = analyze_product_categories(df)

    assert len(unique_categories) == 1, "Expected 1 unique category"

    assert df_category_counts.iloc[0]['Count'] == 3, "Expected 3 products in 'Electronics' category"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_single_category()
    print("All tests passed!")
