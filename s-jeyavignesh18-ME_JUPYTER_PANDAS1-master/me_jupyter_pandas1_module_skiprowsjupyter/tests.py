import pandas as pd
from solution import load_exam_review_skiprows, load_exam_review_skip_specific_rows

def test_load_exam_review_skiprows():
    """Test function for load_exam_review_skiprows to verify correct data loading and skipped rows."""
    full_df = pd.read_csv('https://gitlab.crio.do/public_content/da-ds-datasets/pyt-102-datasets/-/raw/main/exam_review.csv', sep='>')
    exam_df = load_exam_review_skiprows()
    assert len(exam_df) == len(full_df) - 2, "Skipping rows failed: Row count mismatch"
    print("✅ Test Passed: Exam review data loaded successfully, and first 2 rows were skipped.")
    print(exam_df.head())

def test_load_exam_review_skip_specific_rows():
    """Test function for load_exam_review_skip_specific_rows to verify correct data loading, column count, and skipped rows."""
    full_df = pd.read_csv('https://gitlab.crio.do/public_content/da-ds-datasets/pyt-102-datasets/-/raw/main/exam_review.csv', sep='>', skip_blank_lines=False)
    exam_df = load_exam_review_skip_specific_rows()
    assert not exam_df.empty, "Exam review data loading failed (custom separator '>', skipping rows [1,3])"
    assert exam_df.shape[1] == 5, f"Column count mismatch: Expected 5, but found {exam_df.shape[1]}"
    skipped_rows = full_df.iloc[[1, 3]]
    for _, skipped_row in skipped_rows.iterrows():
        assert not (exam_df == skipped_row).all(axis=1).any(), f"Skipping rows failed: Row {skipped_row} still exists in the dataset."
    print("✅ Test Passed: Exam review data loaded successfully, with correct column count (5), and rows [1,3] were skipped.")
    print(exam_df.head())