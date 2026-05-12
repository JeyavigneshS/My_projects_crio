import pandas as pd
from solution import load_exam_review_selected_columns, load_exam_review_selected_columns_by_index

def test_load_exam_review_selected_columns():
    """Test function for load_exam_review_selected_columns to verify correct data loading and column selection."""
    exam_df = load_exam_review_selected_columns()
    assert not exam_df.empty, "Exam review data loading failed (custom separator '>', selected columns ['first_name', 'last_name', 'age'])"
    expected_columns = {'first_name', 'last_name', 'age'}
    actual_columns = set(exam_df.columns)
    assert actual_columns == expected_columns, f"Column mismatch: Expected {expected_columns}, but found {actual_columns}"
    print("✅ Test Passed: Exam review data loaded successfully with correct column selection ('first_name', 'last_name', 'age').")
    print(exam_df.head())

def test_load_exam_review_selected_columns_by_index():
    """Test function for load_exam_review_selected_columns_by_index to verify correct data loading and column selection by index."""
    full_df = pd.read_csv('https://gitlab.crio.do/public_content/da-ds-datasets/pyt-102-datasets/-/raw/main/exam_review.csv', sep='>', skip_blank_lines=False)
    exam_df = load_exam_review_selected_columns_by_index()
    assert not exam_df.empty, "Exam review data loading failed (custom separator '>', selected columns [0,1,2])"
    expected_columns = list(full_df.columns[:3])
    actual_columns = list(exam_df.columns)
    assert actual_columns == expected_columns, f"Column mismatch: Expected {expected_columns}, but found {actual_columns}"
    print("✅ Test Passed: Exam review data loaded successfully with correct column selection (indexes 0,1,2).")
    print(exam_df.head())
