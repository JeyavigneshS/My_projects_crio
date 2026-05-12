import pandas as pd
import inspect
from solution import analyze_employee_salaries  # Ensure the function is implemented in solution.py

def test_analyze_employee_salaries():
    """Test analyze_employee_salaries function using actual dataset."""

    # Dataset URL
    file_path = "https://gitlab.crio.do/root/me_jupyter_numpy_pandas_interview_prep_datasets/-/raw/master/employee_salaries.csv"

    # Call the function and capture returned DataFrame
    sorted_df = analyze_employee_salaries(file_path)

    # Check return type
    assert isinstance(sorted_df, pd.DataFrame), "Function should return a DataFrame"

    # Check required columns exist
    expected_columns = {"name", "salary", "role", "department"}
    assert expected_columns.issubset(set(sorted_df.columns.str.lower())), "Missing required columns"

    # Check that DataFrame is sorted in descending order of salary
    sorted_salaries = sorted_df['salary'].tolist()
    assert sorted_salaries == sorted(sorted_salaries, reverse=True), "DataFrame not sorted by salary descending"

    # Optional check: average salary for Data Analysts is correctly calculated
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    expected_avg = df[df['role'].str.lower() == 'data analyst']['salary'].mean()
    actual_avg = df[df['role'].str.lower() == 'data analyst']['salary'].mean()
    assert round(expected_avg, 2) == round(actual_avg, 2), "Average salary for Data Analysts is incorrect"

    # Optional check: ensure filter for Finance employees with > $70,000 works
    finance_high = df[(df['salary'] > 70000) & (df['department'].str.lower() == 'finance')]
    assert not finance_high.empty, "No high earners found in Finance, but some should exist"

    print("✅ Test Passed: analyze_employee_salaries() works correctly with the dataset.")
