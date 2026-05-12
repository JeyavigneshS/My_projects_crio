from solution import modify_order

def test_modify_order_regular_case():
    order = ['apple', 'banana', 'carrot']
    expected_modified = ['orange', 'banana', 'carrot']  # Replaced 'apple' with 'orange'
    expected_original = ['apple', 'banana', 'carrot']
    
    modified, original = modify_order(order)
    
    assert modified == expected_modified, f"Expected {expected_modified}, but got {modified}"
    assert original == expected_original, f"Expected {expected_original}, but got {original}"

def test_modify_order_already_in_alternatives():
    order = ['orange', 'banana', 'carrot']
    expected_modified = ['mango', 'banana', 'carrot']  # Replaced 'orange' with 'mango'
    expected_original = ['orange', 'banana', 'carrot']
    
    modified, original = modify_order(order)
    
    assert modified == expected_modified, f"Expected {expected_modified}, but got {modified}"
    assert original == expected_original, f"Expected {expected_original}, but got {original}"

def test_modify_order_first_ingredient_is_banana():
    order = ['banana', 'apple', 'carrot']
    expected_modified = ['orange', 'apple', 'carrot']  # Replaced 'banana' with 'orange'
    expected_original = ['banana', 'apple', 'carrot']
    
    modified, original = modify_order(order)
    
    assert modified == expected_modified, f"Expected {expected_modified}, but got {modified}"
    assert original == expected_original, f"Expected {expected_original}, but got {original}"

def test_modify_order_empty_order():
    order = []
    expected_modified = []
    expected_original = []
    
    modified, original = modify_order(order)
    
    assert modified == expected_modified, f"Expected {expected_modified}, but got {modified}"
    assert original == expected_original, f"Expected {expected_original}, but got {original}"

