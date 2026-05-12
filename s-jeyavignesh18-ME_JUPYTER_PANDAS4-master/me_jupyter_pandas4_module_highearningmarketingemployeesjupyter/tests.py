import pandas as pd
from solution import filter_marketing_high_salary

def test_standard_case():
    data = {
        'Employee': ['Alice Smith', 'Bob Johnson', 'Carol Evans', 'David Brown', 'Emily Davis'],
        'Department': ['Marketing', 'Sales', 'Marketing', 'Marketing', 'HR'],
        'Salary': [55000, 48000, 49000, 60000, 52000]
    }
    df = pd.DataFrame(data)

    df_filtered = filter_marketing_high_salary(df)

    assert 'Employee' in df_filtered.columns, "Expected 'Employee' column"

    assert df_filtered.shape[0] == 2, "Expected 2 employees in the filtered DataFrame"

    assert 'Alice Smith' in df_filtered['Employee'].values, "Expected 'Alice Smith' to be in the filtered DataFrame"

    assert 'David Brown' in df_filtered['Employee'].values, "Expected 'David Brown' to be in the filtered DataFrame"


def test_edge_case_empty_dataset():
    df = pd.DataFrame(columns=['Employee', 'Department', 'Salary'])
    df_filtered = filter_marketing_high_salary(df)
    assert df_filtered.empty, "Expected an empty DataFrame"

def test_no_high_salary_marketing_employees():
    data = {
        'Employee': ['A', 'B', 'C'],
        'Department': ['Marketing', 'Marketing', 'Marketing'],
        'Salary': [40000, 45000, 49000]
    }
    df = pd.DataFrame(data)

    df_filtered = filter_marketing_high_salary(df)

    assert df_filtered.empty, "Expected an empty DataFrame when no Marketing employees earn above $50,000"


if __name__ == "__main__":
    test_standard_case()
    test_edge_case_empty_dataset()
    test_no_high_salary_marketing_employees()
    print("All tests passed!")
