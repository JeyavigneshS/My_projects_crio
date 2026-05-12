from solution import update_inventory, print_inventory_2d
import numpy as np

def test_update_inventory_addition():
    inventory_matrix = np.array([
        [10,  5,  2,  0],  # Widget
        [ 3, 15,  8,  4],  # Gadget
        [ 0,  5,  1, 10],  # Gizmo
    ], dtype=int)

    new_shipments_2d = np.array([
        [ 2,  1,  0,  5],  # Widget
        [ 0,  2,  1,  0],  # Gadget
        [ 4,  0,  0,  2],  # Gizmo
    ], dtype=int)

    expected_inventory = np.array([
        [12,  6,  2,  5],  # Widget
        [ 3, 17,  9,  4],  # Gadget
        [ 4,  5,  1, 12],  # Gizmo
    ], dtype=int)

    updated_inventory = update_inventory(inventory_matrix, new_shipments_2d, add=True)

    assert np.array_equal(updated_inventory, expected_inventory), f"Expected {expected_inventory}, but got {updated_inventory}"
    print("✅ Test Passed: Inventory updated correctly after adding new shipments.")

    print_inventory_2d(updated_inventory, "Test Case: After Adding New Shipments")

def test_update_inventory_subtraction():
    inventory_matrix = np.array([
        [12,  6,  2,  5],  # Widget
        [ 3, 17,  9,  4],  # Gadget
        [ 4,  5,  1, 12],  # Gizmo
    ], dtype=int)

    shipped_out_2d = np.array([
        [ 0,  2,  1,  0],  # Widget
        [ 1,  0,  2,  2],  # Gadget
        [ 0,  1,  1,  3],  # Gizmo
    ], dtype=int)

    expected_inventory = np.array([
        [12,  4,  1,  5],  # Widget
        [ 2, 17,  7,  2],  # Gadget
        [ 4,  4,  0,  9],  # Gizmo
    ], dtype=int)

    updated_inventory = update_inventory(inventory_matrix, shipped_out_2d, add=False)

    assert np.array_equal(updated_inventory, expected_inventory), f"Expected {expected_inventory}, but got {updated_inventory}"
    print("✅ Test Passed: Inventory updated correctly after shipping out stock.")

    print_inventory_2d(updated_inventory, "Test Case: After Shipping Out Stock")

def test_update_inventory_no_change():
    inventory_matrix = np.array([
        [10,  5,  2,  0],  # Widget
        [ 3, 15,  8,  4],  # Gadget
        [ 0,  5,  1, 10],  # Gizmo
    ], dtype=int)

    no_updates = np.zeros((3, 4), dtype=int)

    expected_inventory = inventory_matrix.copy()

    updated_inventory = update_inventory(inventory_matrix, no_updates, add=True)

    assert np.array_equal(updated_inventory, expected_inventory), f"Expected {expected_inventory}, but got {updated_inventory}"
    print("✅ Test Passed: Inventory remains unchanged when no updates are applied.")

    print_inventory_2d(updated_inventory, "Test Case: No Change in Inventory")
