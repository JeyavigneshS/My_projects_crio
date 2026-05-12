import pandas as pd
from solution import analyze_canceled_shipments  # Ensure solution.py contains the implemented function

def test_analyze_canceled_shipments():
    """Test function with valid canceled shipments from January to March 2024."""
    test_data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6],
        'shipment_date': ['2024-01-10', '2024-02-15', '2024-03-01', '2024-03-08', '2024-04-06', '2024-04-07'],
        'status': ['Cancelled', 'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled']
    })

    expected_output = {
        '2024-01': 1,
        '2024-02': 1,
        '2024-03': 2
    }

    result = analyze_canceled_shipments(test_data)
    assert result == expected_output

def test_no_canceled_shipments():
    """Test function when no shipments are canceled."""
    test_data = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'shipment_date': ['2024-01-05', '2024-02-12', '2024-03-20', '2024-03-25'],
        'status': ['Delivered', 'In Transit', 'Pending', 'Delivered']
    })

    result = analyze_canceled_shipments(test_data)
    assert result == {}

test_analyze_canceled_shipments()
test_no_canceled_shipments()
test_shipments_outside_fixed_period()
print("✅ All tests passed.")
