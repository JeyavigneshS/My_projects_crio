import pandas as pd
from solution import rank_students

def test_standard_case():
    data = {
        'Student': ['John', 'Sarah', 'Tom', 'Emma', 'Mark', 'Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Math': [94, 97, 50, 53, 53, 69, 57, 77, 93, 85],
        'Science': [74, 67, 87, 75, 63, 68, 76, 92, 89, 88],
        'English': [64, 89, 82, 51, 59, 90, 78, 81, 91, 83]
    }
    df = pd.DataFrame(data)

    df_ranked = rank_students(df)

    # Convert ranking columns to integers to avoid float comparison issues
    rank_columns = ['Rank_Avg', 'Rank_Min', 'Rank_Max', 'Rank_Dense']
    df_ranked[rank_columns] = df_ranked[rank_columns].astype(int)

    assert 'Total Score' in df_ranked.columns, "Expected 'Total Score' column in result"
    assert 'Rank_Avg' in df_ranked.columns, "Expected 'Rank_Avg' column in result"
    assert 'Rank_Min' in df_ranked.columns, "Expected 'Rank_Min' column in result"
    assert 'Rank_Max' in df_ranked.columns, "Expected 'Rank_Max' column in result"
    assert 'Rank_Dense' in df_ranked.columns, "Expected 'Rank_Dense' column in result"


def test_ranking_consistency():
    data = {
        'Student': ['A', 'B', 'C'],
        'Math': [90, 80, 80],
        'Science': [90, 80, 80],
        'English': [90, 80, 80]
    }
    df = pd.DataFrame(data)

    df_ranked = rank_students(df)

    # Convert ranking columns to integers to ensure consistency
    rank_columns = ['Rank_Avg', 'Rank_Min', 'Rank_Max', 'Rank_Dense']
    df_ranked[rank_columns] = df_ranked[rank_columns].astype(int)

    assert df_ranked.iloc[0]['Rank_Min'] == 1, "Expected highest score to be ranked 1"
    assert df_ranked.iloc[1]['Rank_Max'] == 2, "Expected tied ranks to be handled correctly"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_ranking_consistency()
    print("✅ All tests passed!")
