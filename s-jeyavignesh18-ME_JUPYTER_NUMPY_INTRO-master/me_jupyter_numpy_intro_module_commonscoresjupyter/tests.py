from solution import calculate_mode

def test_calculate_mode_regular_case():
    scores = [90, 80, 85, 70, 95, 85]
    expected_mode = 85  # The most frequent score is 85
    
    try:
        mode = calculate_mode(scores)
        assert mode == expected_mode, f"Expected {expected_mode}, but got {mode}"
        print('✅ Test Passed: Mode is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

def test_calculate_mode_multiple_modes():
    scores = [100, 100, 90, 80, 70, 60, 70, 70]
    expected_mode = 70  # The most frequent score is 70
    
    try:
        mode = calculate_mode(scores)
        assert mode == expected_mode, f"Expected {expected_mode}, but got {mode}"
        print('✅ Test Passed: Mode is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

def test_calculate_mode_single_score():
    scores = [95]
    expected_mode = 95  # The only score in the list is the mode
    
    try:
        mode = calculate_mode(scores)
        assert mode == expected_mode, f"Expected {expected_mode}, but got {mode}"
        print('✅ Test Passed: Mode is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

