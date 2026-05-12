import pandas as pd
from solution import analyze_product_categories

def test_standard_case():
    data = {
        'Product': ['TV', 'Laptop', 'Phone', 'Headphones', 'Blender'],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Home'],
        'Sales': [2000, 3000, 500, 1200, 2500]
    }
    df = pd.DataFrame(data)

    num_categories, unique_categories, category_counts = analyze_product_categories(df)

    assert num_categories == 2, "Expected 2 unique categories"

    assert 'Electronics' in unique_categories, "Expected 'Electronics' in category list"

    assert 'Home' in unique_categories, "Expected 'Home' in category list"

    assert category_counts['Electronics'] == 4, "Expected 4 products in 'Electronics' category"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Product', 'Category', 'Sales'])
    num_categories, unique_categories, category_counts = analyze_product_categories(df)
    assert num_categories == 0, "Expected 0 unique categories"
    assert unique_categories == [], "Expected an empty category list"
    assert category_counts == {}, "Expected an empty dictionary for category counts"

def test_duplicate_entries():
    data = {
        'Product': ['TV', 'TV', 'Laptop', 'Laptop', 'Phone'],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
        'Sales': [2000, 2000, 3000, 3000, 500]
    }
    df = pd.DataFrame(data)

    num_categories, unique_categories, category_counts = analyze_product_categories(df)

    assert num_categories == 1, "Expected 1 unique category"

    assert category_counts['Electronics'] == 3, "Expected 3 unique products after duplicate removal"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_duplicate_entries()
    print("All tests passed!")
