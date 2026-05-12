from solution import calculate_mean

def test_calculate_mean_regular_case():
    scores = [90, 80, 85, 70, 95]
    expected_mean = 84.0  # The average of [90, 80, 85, 70, 95] is 84.0
    
    mean_result = calculate_mean(scores)
    
    assert mean_result == expected_mean, f"Expected {expected_mean}, but got {mean_result}"
    print('✅ Test Passed: Mean calculated correctly.')

def test_calculate_mean_single_value():
    scores = [100]
    expected_mean = 100.0  # The average of a single score [100] is 100.0
    
    mean_result = calculate_mean(scores)
    
    assert mean_result == expected_mean, f"Expected {expected_mean}, but got {mean_result}"
    print('✅ Test Passed: Mean calculated correctly for single value.')

def test_calculate_mean_empty_list():
    scores = []
    expected_mean = float('nan')  # Mean of an empty list should return NaN (Not a Number)
    
    mean_result = calculate_mean(scores)
    
    assert mean_result != mean_result, "Expected NaN, but got a number"
    print('✅ Test Passed: Mean correctly returns NaN for an empty list.')

