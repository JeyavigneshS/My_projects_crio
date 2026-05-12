from solution import update_inventory, print_inventory

def test_update_inventory_addition():
    products = ["Widget", "Gadget", "Gizmo"]
    
    # Initial warehouse quantities
    central_warehouse = [10, 3, 0]
    north_warehouse = [5, 15, 5]
    south_warehouse = [2, 8, 1]
    west_warehouse = [0, 4, 10]

    # New shipments to add
    new_shipments_central = [2, 0, 4]
    new_shipments_north = [1, 2, 0]
    new_shipments_south = [0, 1, 0]
    new_shipments_west = [5, 0, 2]

    new_shipments = [new_shipments_central, new_shipments_north, new_shipments_south, new_shipments_west]

    # Expected inventory after addition
    expected_central = [12, 3, 4]
    expected_north = [6, 17, 5]
    expected_south = [2, 9, 1]
    expected_west = [5, 4, 12]

    # Apply inventory update
    central_warehouse, north_warehouse, south_warehouse, west_warehouse = update_inventory(
        central_warehouse, north_warehouse, south_warehouse, west_warehouse, new_shipments, add=True
    )

    # Assertions
    assert central_warehouse == expected_central, f"Expected {expected_central}, but got {central_warehouse}"
    assert north_warehouse == expected_north, f"Expected {expected_north}, but got {north_warehouse}"
    assert south_warehouse == expected_south, f"Expected {expected_south}, but got {south_warehouse}"
    assert west_warehouse == expected_west, f"Expected {expected_west}, but got {west_warehouse}"

    print("✅ Test Passed: Inventory updated correctly after adding new shipments.")

def test_update_inventory_subtraction():
    products = ["Widget", "Gadget", "Gizmo"]

    # Initial warehouse quantities
    central_warehouse = [12, 3, 4]
    north_warehouse = [6, 17, 5]
    south_warehouse = [2, 9, 1]
    west_warehouse = [5, 4, 12]

    # Shipped-out quantities
    shipped_out_central = [0, 1, 0]
    shipped_out_north = [2, 0, 1]
    shipped_out_south = [1, 2, 1]
    shipped_out_west = [0, 2, 3]

    shipped_out = [shipped_out_central, shipped_out_north, shipped_out_south, shipped_out_west]

    # Expected inventory after subtraction
    expected_central = [12, 2, 4]
    expected_north = [4, 17, 4]
    expected_south = [1, 7, 0]
    expected_west = [5, 2, 9]

    # Apply inventory update
    central_warehouse, north_warehouse, south_warehouse, west_warehouse = update_inventory(
        central_warehouse, north_warehouse, south_warehouse, west_warehouse, shipped_out, add=False
    )

    # Assertions
    assert central_warehouse == expected_central, f"Expected {expected_central}, but got {central_warehouse}"
    assert north_warehouse == expected_north, f"Expected {expected_north}, but got {north_warehouse}"
    assert south_warehouse == expected_south, f"Expected {expected_south}, but got {south_warehouse}"
    assert west_warehouse == expected_west, f"Expected {expected_west}, but got {west_warehouse}"

    print("✅ Test Passed: Inventory updated correctly after shipping out stock.")
    
# Run tests
try:
    test_update_inventory_addition()
    test_update_inventory_subtraction()
except Exception as e:
    print(f"❌ Test Failed: {e}")

