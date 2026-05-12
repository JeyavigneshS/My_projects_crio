from solution import transpose_sales_data

def test_transpose_sales_data_regular_case():
    sales_matrix = [[200, 180, 220],
                    [150, 170, 160],
                    [300, 320, 310]]
    
    expected_output = [[200, 150, 300],
                       [180, 170, 320],
                       [220, 160, 310]]
    
    output = transpose_sales_data(sales_matrix)
    
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_transpose_sales_data_single_row():
    sales_matrix = [[100, 200, 300]]
    
    expected_output = [[100],
                       [200],
                       [300]]
    
    output = transpose_sales_data(sales_matrix)
    
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_transpose_sales_data_single_column():
    sales_matrix = [[100],
                    [200],
                    [300]]
    
    expected_output = [[100, 200, 300]]
    
    output = transpose_sales_data(sales_matrix)
    
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_transpose_sales_data_empty_matrix():
    sales_matrix = []
    
    expected_output = []
    
    output = transpose_sales_data(sales_matrix)
    
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

