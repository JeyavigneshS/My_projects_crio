import pandas as pd
import inspect
from solution import create_and_modify_website_traffic

def test_create_and_modify_website_traffic():
    """Test function for create_and_modify_website_traffic to verify correct Series creation and updates."""
    website_traffic, march_traffic, boosted_traffic = create_and_modify_website_traffic()

    # Ensure the Series is not empty
    assert not website_traffic.empty, "Website traffic Series creation failed (empty Series)"

    # Ensure the correct traffic value is accessed for March
    assert march_traffic == 58, f"Incorrect March traffic: Expected 58, but found {march_traffic}"

    # Ensure June traffic is updated correctly
    assert website_traffic["June"] == 100, f"June traffic update failed: Expected 100, but found {website_traffic['June']}"

    # Ensure a 5% increase was applied correctly
    expected_boosted_values = website_traffic * 1.05
    assert boosted_traffic.equals(expected_boosted_values), "Boosted traffic values are incorrect"

    # Ensure function contains necessary operations
    function_source = inspect.getsource(create_and_modify_website_traffic)
    assert '* 1.05' in function_source, "5% increase is not applied in the function"

    print("✅ Test Passed: Website traffic data created, updated, and boosted correctly.")
    print("🔍 Updated Website Traffic:")
    print(website_traffic)
    print("🔍 Website Traffic After 5% Boost:")
    print(boosted_traffic)