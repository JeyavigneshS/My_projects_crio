import pandas as pd
from solution import load_exam_review

def test_load_exam_review():
    """Test function for load_exam_review to verify correct data loading and column count."""
    exam_df = load_exam_review()

    # Check if DataFrame is not empty
    assert not exam_df.empty, "Exam review data loading failed (custom separator '>')"

    # Check if the DataFrame has exactly 5 columns
    assert exam_df.shape[1] == 5, f"Column count mismatch: Expected 5, but found {exam_df.shape[1]}"

    print("✅ Test Passed: Exam review data loaded successfully with correct column count (5).")

    # Display first few rows
    print(exam_df.head())
