import pandas as pd
from solution import load_products_excel, load_products_excel_with_index, load_all_sheets

def test_load_products_excel():
    """Test function for load_products_excel to verify correct data loading."""
    products_df = load_products_excel()
    assert not products_df.empty, "Product data loading failed (Excel file is empty)"
    assert products_df.shape[1] > 0, "Product data loading failed (No columns found)"
    print("✅ Test Passed: Products data loaded successfully from Excel file.")
    print(products_df.head())

def test_load_products_excel_with_index():
    """Test function for load_products_excel_with_index to verify correct data loading."""
    products_df = load_products_excel_with_index()
    assert not products_df.empty, "Product data loading failed (Excel file is empty or incorrect sheet)"
    assert products_df.shape[1] > 0, "Product data loading failed (No columns found)"
    assert products_df.index.name == 'product_id', f"Index column mismatch: Expected 'product_id', but found {products_df.index.name}"
    print("✅ Test Passed: Products data loaded successfully from Excel file with correct index.")
    print(products_df.head())

def test_load_all_sheets():
    """Test function for load_all_sheets to verify correct data loading."""
    sheets_dict = load_all_sheets()
    assert sheets_dict, "Sheet loading failed (Excel file might be empty or incorrect path)"
    expected_sheets = {'Products', 'Merchants'}
    actual_sheets = set(sheets_dict.keys())
    assert expected_sheets.issubset(actual_sheets), f"Missing sheets: Expected {expected_sheets}, but found {actual_sheets}"
    products_df = sheets_dict['Products']
    merchants_df = sheets_dict['Merchants']
    assert not products_df.empty, "Products sheet is empty"
    assert not merchants_df.empty, "Merchants sheet is empty"
    print("✅ Test Passed: All sheets loaded successfully, and required sheets contain data.")
    print("### Products Sheet:")
    print(products_df.head())
    print("### Merchants Sheet:")
    print(merchants_df.head())
