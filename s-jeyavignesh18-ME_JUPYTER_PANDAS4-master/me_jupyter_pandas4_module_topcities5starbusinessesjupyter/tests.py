import pandas as pd
from solution import analyze_5star_businesses

def test_standard_case():
    data = {
        'Business': ['Cafe Delight', 'Urban Eatery', 'Sea Breeze', 'Mountain Dine', 'Lakeside Inn', 'City Bistro'],
        'City': ['New York', 'New York', 'Miami', 'Denver', 'Denver', 'New York'],
        'Rating': [5, 4, 5, 5, 5, 5]
    }
    df = pd.DataFrame(data)

    df_ranked_cities = analyze_5star_businesses(df)

    assert 'Count of 5-Star Businesses' in df_ranked_cities.columns, "Expected 'Count of 5-Star Businesses' column"

    assert df_ranked_cities.iloc[0]['City'] == 'New York', "Expected 'New York' to be ranked first"

    assert df_ranked_cities.iloc[0]['Count of 5-Star Businesses'] == 2, "Expected count to be 2 for 'New York'"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Business', 'City', 'Rating'])
    df_ranked_cities = analyze_5star_businesses(df)
    assert df_ranked_cities.empty, "Expected an empty DataFrame"

def test_no_5star_businesses():
    data = {
        'Business': ['A', 'B', 'C'],
        'City': ['Chicago', 'Los Angeles', 'San Francisco'],
        'Rating': [3, 4, 2]
    }
    df = pd.DataFrame(data)

    df_ranked_cities = analyze_5star_businesses(df)

    assert df_ranked_cities.empty, "Expected an empty DataFrame when no 5-star businesses are present"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_no_5star_businesses()
    print("All tests passed!")
