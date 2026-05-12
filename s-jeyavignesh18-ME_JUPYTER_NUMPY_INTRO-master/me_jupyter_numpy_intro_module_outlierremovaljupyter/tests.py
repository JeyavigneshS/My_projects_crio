from solution import calculate_median

def test_calculate_median_odd_number_of_elements():
    scores = [90, 80, 85, 70, 95]
    expected_median = 85.0  # Median of sorted list [70, 80, 85, 90, 95] is 85
    
    median = calculate_median(scores)
    
    assert median == expected_median, f"Expected {expected_median}, but got {median}"

def test_calculate_median_even_number_of_elements():
    scores = [100, 100, 90, 80, 70, 60]
    expected_median = 85.0  # Median of sorted list [60, 70, 80, 90, 100, 100] is (80+90)/2 = 85
    
    median = calculate_median(scores)
    
    assert median == expected_median, f"Expected {expected_median}, but got {median}"

def test_calculate_median_single_element():
    scores = [75]
    expected_median = 75.0  # Median of a single element is the element itself
    
    median = calculate_median(scores)
    
    assert median == expected_median, f"Expected {expected_median}, but got {median}"

def test_calculate_median_empty_list():
    scores = []
    expected_median = float('nan')  # Median of an empty list is undefined (NaN in NumPy)
    
    median = calculate_median(scores)
    
    assert median != median, f"Expected NaN, but got {median}"  # Checking for NaN (since NaN is not equal to itself)

