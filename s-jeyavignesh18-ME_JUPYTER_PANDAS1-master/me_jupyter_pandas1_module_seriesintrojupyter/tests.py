import pandas as pd
from solution import test_create_monthly_sales_series, test_get_sales_for_month, test_update_sales_for_month, test_increase_sales_by_percentage

def test_create_monthly_sales_series():
    try:
        sales = create_monthly_sales_series()
        assert not sales.empty, "Sales series is empty"
        assert list(sales.index) == ["January", "February", "March", "April", "May", "June"], "Month index mismatch"
        assert list(sales.values) == [200, 300, 250, 400, 350, 500], "Sales values mismatch"

        print("\n✅ Test Passed: Monthly Sales Series created successfully.")
        print(sales)
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")

def test_get_sales_for_month():
    try:
        sales = create_monthly_sales_series()
        march_sales = get_sales_for_month(sales)
        assert march_sales == 250, "Incorrect sales value for March"

        print("\n✅ Test Passed: Sales for March retrieved successfully.")
        print(f"Sales in March: {march_sales}")
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")

def test_update_sales_for_month():
    try:
        sales = create_monthly_sales_series()
        updated_sales = update_sales_for_month(sales)
        assert updated_sales["June"] == 550, "June sales update failed"

        print("\n✅ Test Passed: Sales for June updated successfully.")
        print(updated_sales)
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")

def test_increase_sales_by_percentage():
    try:
        sales = create_monthly_sales_series()
        increased_sales = increase_sales_by_percentage(sales)
        expected_values = [value * 1.10 for value in sales.values]
        assert all(increased_sales.values == expected_values), "Sales increase calculation incorrect"

        print("\n✅ Test Passed: Sales increased by 10% successfully.")
        print(increased_sales)
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
