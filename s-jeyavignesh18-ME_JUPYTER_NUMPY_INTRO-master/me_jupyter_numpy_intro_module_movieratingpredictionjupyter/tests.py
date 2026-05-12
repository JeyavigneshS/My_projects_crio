from solution import predict_rating, predict_rating_numpy
import numpy as np

def test_predict_rating_basic():
    ratings = np.array([
        [4, 5, np.nan],
        [2, 3, 5],
        [5, 5, 4]
    ])
    user_index = 0
    movie_index = 2
    expected = 4.5  # Average of [5, 4]

    # Test predict_rating function
    result = predict_rating(ratings, user_index, movie_index)
    assert np.isclose(result, expected, equal_nan=True), f"predict_rating failed: Expected {expected}, but got {result}"

    # Test predict_rating_numpy function
    result = predict_rating_numpy(ratings, user_index, movie_index)
    assert np.isclose(result, expected, equal_nan=True), f"predict_rating_numpy failed: Expected {expected}, but got {result}"

def test_predict_rating_no_valid_ratings():
    ratings = np.array([
        [4, 5, np.nan],
        [2, 3, np.nan],
        [5, 5, np.nan]
    ])
    user_index = 0
    movie_index = 2
    expected = np.nan  # No valid ratings for this movie

    # Test predict_rating function
    result = predict_rating(ratings, user_index, movie_index)
    assert np.isnan(result), f"predict_rating failed: Expected NaN, but got {result}"

    # Test predict_rating_numpy function
    result = predict_rating_numpy(ratings, user_index, movie_index)
    assert np.isnan(result), f"predict_rating_numpy failed: Expected NaN, but got {result}"

def test_predict_rating_partial_ratings():
    ratings = np.array([
        [4, np.nan, 3],
        [2, 3, 5],
        [5, 5, np.nan]
    ])
    user_index = 0
    movie_index = 1
    expected = 4.0  # Average of [3, 5]

    # Test predict_rating function
    result = predict_rating(ratings, user_index, movie_index)
    assert np.isclose(result, expected, equal_nan=True), f"predict_rating failed: Expected {expected}, but got {result}"

    # Test predict_rating_numpy function
    result = predict_rating_numpy(ratings, user_index, movie_index)
    assert np.isclose(result, expected, equal_nan=True), f"predict_rating_numpy failed: Expected {expected}, but got {result}"

def test_predict_rating_incorrect_expected():
    ratings = np.array([
        [4, 5, np.nan],
        [2, 3, 5],
        [5, 5, 4]
    ])
    user_index = 0
    movie_index = 2
    incorrect_expected = 3.0  # Incorrect expected output to test failure

    # Test predict_rating function
    result = predict_rating(ratings, user_index, movie_index)
    assert not np.isclose(result, incorrect_expected, equal_nan=True), f"predict_rating failed: Expected not {incorrect_expected}, but got {result}"

    # Test predict_rating_numpy function
    result = predict_rating_numpy(ratings, user_index, movie_index)
    assert not np.isclose(result, incorrect_expected, equal_nan=True), f"predict_rating_numpy failed: Expected not {incorrect_expected}, but got {result}"
