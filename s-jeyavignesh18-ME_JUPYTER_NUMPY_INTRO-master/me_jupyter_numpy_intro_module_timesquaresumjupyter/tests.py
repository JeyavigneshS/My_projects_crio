from solution import sum_of_squares_list, sum_of_squares_numpy

def test_sum_of_squares_list():
    # Test 1: Regular case for sum_of_squares_list
    n = 5
    expected_sum = sum([i ** 2 for i in range(1, n + 1)])  # Manually calculate the expected sum
    list_sum = sum_of_squares_list(n)
    assert list_sum == expected_sum, f"Expected {expected_sum}, but got {list_sum}"

def test_sum_of_squares_numpy():
    # Test 2: Regular case for sum_of_squares_numpy
    n = 5
    expected_sum = sum([i ** 2 for i in range(1, n + 1)])  # Manually calculate the expected sum
    numpy_sum = sum_of_squares_numpy(n)
    assert numpy_sum == expected_sum, f"Expected {expected_sum}, but got {numpy_sum}"

def test_sum_of_squares_large_case_list():
    # Test 3: Large input (n = 100) for list-based function
    n = 100
    expected_sum = sum([i ** 2 for i in range(1, n + 1)])
    list_sum = sum_of_squares_list(n)
    assert list_sum == expected_sum, f"Expected {expected_sum}, but got {list_sum}"

def test_sum_of_squares_large_case_numpy():
    # Test 4: Large input (n = 100) for NumPy-based function
    n = 100
    expected_sum = sum([i ** 2 for i in range(1, n + 1)])
    numpy_sum = sum_of_squares_numpy(n)
    assert numpy_sum == expected_sum, f"Expected {expected_sum}, but got {numpy_sum}"

def test_sum_of_squares_both_functions():
    # Test 5: Compare the outputs of both functions for the same n
    n = 100
    list_sum = sum_of_squares_list(n)
    numpy_sum = sum_of_squares_numpy(n)
    assert list_sum == numpy_sum, f"Expected {list_sum} from list-based and {numpy_sum} from NumPy, but they differ"

