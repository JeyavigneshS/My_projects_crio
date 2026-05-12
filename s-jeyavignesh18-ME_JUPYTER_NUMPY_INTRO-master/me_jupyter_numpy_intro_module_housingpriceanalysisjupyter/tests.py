from solution import has_outliers, find_central_tendency

def test_has_outliers_with_outliers():
    prices = [200000, 250000, 300000, 1000000, 1200000]
    expected_output = True
    
    result = has_outliers(prices)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_has_outliers_without_outliers():
    prices = [200000, 250000, 300000, 500000]
    expected_output = False
    
    result = has_outliers(prices)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_find_central_tendency_with_outliers():
    prices = [200000, 250000, 300000, 1000000, 1200000]
    expected_output = "Median: 300000"
    
    result = find_central_tendency(prices)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_find_central_tendency_without_outliers():
    prices = [200000, 250000, 300000, 500000]
    expected_output = "Mean: 312500"
    
    result = find_central_tendency(prices)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_find_central_tendency_all_same_values():
    prices = [500000, 500000, 500000, 500000, 500000]
    expected_output = "Mode: 500000"
    
    result = find_central_tendency(prices)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

