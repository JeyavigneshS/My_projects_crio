from solution import memory_usage_list, memory_usage_numpy

def test_memory_usage_small_n():
    # Test for a small value of n
    n = 100
    list_mem_usage = memory_usage_list(n)
    np_mem_usage = memory_usage_numpy(n)

    # Check that NumPy array uses less memory than Python list
    assert np_mem_usage < list_mem_usage, f"Test failed: NumPy array should use less memory than Python list. Got {np_mem_usage} vs {list_mem_usage}"
    print("**✅ Test Passed:** NumPy array uses less memory than Python list for n=100")

def test_memory_usage_large_n():
    # Test for a larger value of n
    n = 1000000
    list_mem_usage = memory_usage_list(n)
    np_mem_usage = memory_usage_numpy(n)

    # Check again for larger data
    assert np_mem_usage < list_mem_usage, f"Test failed: NumPy array should use less memory than Python list. Got {np_mem_usage} vs {list_mem_usage}"
    print("**✅ Test Passed:** NumPy array uses less memory than Python list for n=1000000")

def test_memory_usage_empty():
    # Test for empty array/list
    n = 0
    list_mem_usage = memory_usage_list(n)
    np_mem_usage = memory_usage_numpy(n)

    # Check for empty array/list memory usage
    assert np_mem_usage == list_mem_usage, f"Test failed: Memory usage for empty array/list should be the same. Got {np_mem_usage} vs {list_mem_usage}"
    print("**✅ Test Passed:** Memory usage is the same for empty list/array")

def test_memory_usage_identical_for_zero_elements():
    # Check that the memory usage is identical when n is 1 (edge case for minimal elements)
    n = 1
    list_mem_usage = memory_usage_list(n)
    np_mem_usage = memory_usage_numpy(n)

    # Check if the memory usage is reasonable for a single element
    assert np_mem_usage < list_mem_usage, f"Test failed: NumPy array should use less memory than Python list. Got {np_mem_usage} vs {list_mem_usage}"
    print("**✅ Test Passed:** NumPy array uses less memory than Python list for n=1")
