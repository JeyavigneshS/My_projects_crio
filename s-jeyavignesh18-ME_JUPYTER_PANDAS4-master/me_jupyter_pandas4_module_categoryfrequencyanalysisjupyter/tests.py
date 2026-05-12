import pandas as pd
from solution import analyze_category_distribution

def test_standard_case():
    data = {
        'Product': ['TV', 'Blender', 'Smartphone', 'Book', 'Laptop', 'Chair'],
        'Category': ['Electronics', 'Home', 'Electronics', 'Stationery', 'Electronics', 'Home']
    }
    df = pd.DataFrame(data)

    num_categories, category_counts = analyze_category_distribution(df)

    assert num_categories == 3, "Expected 3 unique categories"

    assert category_counts['Electronics'] == 3, "Expected 3 products in 'Electronics' category"

    assert category_counts['Home'] == 2, "Expected 2 products in 'Home' category"

    assert category_counts['Stationery'] == 1, "Expected 1 product in 'Stationery' category"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Product', 'Category'])
    num_categories, category_counts = analyze_category_distribution(df)
    assert num_categories == 0, "Expected 0 unique categories"
    assert category_counts == {}, "Expected an empty dictionary for category counts"

def test_single_category():
    data = {
        'Product': ['Item1', 'Item2', 'Item3'],
        'Category': ['Electronics', 'Electronics', 'Electronics']
    }
    df = pd.DataFrame(data)

    num_categories, category_counts = analyze_category_distribution(df)

    assert num_categories == 1, "Expected 1 unique category"

    assert category_counts['Electronics'] == 3, "Expected 3 products in 'Electronics' category"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_single_category()
    print("All tests passed!")
