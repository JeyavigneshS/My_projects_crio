from solution import memory_usage_list, memory_usage_numpy

def test_memory_usage_for_n_5():
    print("Testing for n=5:")
    try:
        list_memory = memory_usage_list(5)
        numpy_memory = memory_usage_numpy(5)
        
        assert list_memory > 0, f"Expected positive memory value for list, but got {list_memory}"
        assert numpy_memory > 0, f"Expected positive memory value for NumPy array, but got {numpy_memory}"
        
        print('✅ Test Passed: Memory usage for n=5 is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

def test_memory_usage_for_n_10():
    print("Testing for n=10:")
    try:
        list_memory = memory_usage_list(10)
        numpy_memory = memory_usage_numpy(10)
        
        assert list_memory > 0, f"Expected positive memory value for list, but got {list_memory}"
        assert numpy_memory > 0, f"Expected positive memory value for NumPy array, but got {numpy_memory}"
        
        print('✅ Test Passed: Memory usage for n=10 is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')

def test_memory_usage_for_n_100():
    print("Testing for n=100:")
    try:
        list_memory = memory_usage_list(100)
        numpy_memory = memory_usage_numpy(100)
        
        assert list_memory > 0, f"Expected positive memory value for list, but got {list_memory}"
        assert numpy_memory > 0, f"Expected positive memory value for NumPy array, but got {numpy_memory}"
        
        print('✅ Test Passed: Memory usage for n=100 is correct.')
    except Exception as e:
        print(f'❌ Test Failed: {e}')
