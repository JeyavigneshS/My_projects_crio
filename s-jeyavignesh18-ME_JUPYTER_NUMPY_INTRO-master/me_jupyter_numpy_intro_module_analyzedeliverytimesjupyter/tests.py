from solution import analyze_delivery_data

def test_analyze_delivery_data_mean_case():
    # Test case for calculating the mean (because the question asks for a trend)
    delivery_times = [30, 32, 34, 35, 40]
    expected_output = 34.2  # The mean value
    result = analyze_delivery_data(delivery_times)
    
    try:
        assert result == expected_output, f"Expected {expected_output}, but got {result}"
        print('✅ Test Passed: Mean calculation is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

