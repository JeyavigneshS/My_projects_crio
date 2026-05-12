from solution import find_busiest_intersection_numpy, find_busiest_intersection_list
import numpy as np

def test_find_busiest_intersection_regular_case():
    traffic_data = np.array([
        [200, 180, 220],  
        [150, 170, 190],  
        [300, 310, 290]  
    ])
    expected_output = 2  # Intersection 2 has the highest total traffic

    # Test NumPy method
    result_numpy = find_busiest_intersection_numpy(traffic_data)
    assert result_numpy == expected_output, f"Expected {expected_output}, but got {result_numpy}"

    # Test list-based method
    result_list = find_busiest_intersection_list(traffic_data)
    assert result_list == expected_output, f"Expected {expected_output}, but got {result_list}"

def test_find_busiest_intersection_tie_case():
    traffic_data = np.array([
        [100, 100, 100],  
        [150, 150, 150],  
        [150, 150, 150]  
    ])
    expected_output = 1  # The first intersection with max traffic should be chosen

    # Test NumPy method
    result_numpy = find_busiest_intersection_numpy(traffic_data)
    assert result_numpy == expected_output, f"Expected {expected_output}, but got {result_numpy}"

    # Test list-based method
    result_list = find_busiest_intersection_list(traffic_data)
    assert result_list == expected_output, f"Expected {expected_output}, but got {result_list}"

def test_find_busiest_intersection_single_intersection():
    traffic_data = np.array([[500, 600, 700]])  # Only one intersection
    expected_output = 0  # Since there's only one, it must be the busiest

    # Test NumPy method
    result_numpy = find_busiest_intersection_numpy(traffic_data)
    assert result_numpy == expected_output, f"Expected {expected_output}, but got {result_numpy}"

    # Test list-based method
    result_list = find_busiest_intersection_list(traffic_data)
    assert result_list == expected_output, f"Expected {expected_output}, but got {result_list}"

def test_find_busiest_intersection_all_zeroes():
    traffic_data = np.array([
        [0, 0, 0],  
        [0, 0, 0],  
        [0, 0, 0]  
    ])
    expected_output = 0  # All intersections have the same traffic; return the first one

    # Test NumPy method
    result_numpy = find_busiest_intersection_numpy(traffic_data)
    assert result_numpy == expected_output, f"Expected {expected_output}, but got {result_numpy}"

    # Test list-based method
    result_list = find_busiest_intersection_list(traffic_data)
    assert result_list == expected_output, f"Expected {expected_output}, but got {result_list}"

