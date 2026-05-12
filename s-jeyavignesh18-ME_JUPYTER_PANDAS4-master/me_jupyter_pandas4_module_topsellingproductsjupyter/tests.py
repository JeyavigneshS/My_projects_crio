import pandas as pd
from solution import rank_top_products

def test_standard_case():
    data = {
        'Product': ['TV', 'Blender', 'Smartphone', 'Book', 'Laptop'],
        'Category': ['Furniture', 'Home', 'Furniture', 'Electronics', 'Furniture'],
        'Sales': [2079, 3551, 2158, 3948, 4438]
    }
    df = pd.DataFrame(data)

    df_top_products = rank_top_products(df, top_n=3)

    assert 'Rank' in df_top_products.columns, "Expected 'Rank' column"

    assert df_top_products.shape[0] == 3, "Expected top 3 products in the filtered DataFrame"

    assert df_top_products.iloc[0]['Product'] == 'Laptop', "Expected 'Laptop' to be ranked first"

    assert df_top_products.iloc[1]['Product'] == 'Book', "Expected 'Book' to be ranked second"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Product', 'Category', 'Sales'])
    df_top_products = rank_top_products(df, top_n=3)
    assert df_top_products.empty, "Expected an empty DataFrame"

def test_single_product():
    data = {'Product': ['Single Item'], 'Category': ['Electronics'], 'Sales': [5000]}
    df = pd.DataFrame(data)

    df_top_products = rank_top_products(df, top_n=3)

    assert df_top_products.shape[0] == 1, "Expected only 1 product in the filtered DataFrame"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_single_product()
    print("All tests passed!")
