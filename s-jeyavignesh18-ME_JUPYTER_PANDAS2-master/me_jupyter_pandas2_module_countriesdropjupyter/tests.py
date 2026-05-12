import pandas as pd
import inspect
from solution import remove_population_hdi_columns

def test_remove_population_hdi_columns():
    """Test if the 'Population' and 'HDI' columns are removed from the DataFrame."""
    # Check if df.drop() is used in the function
    source_code = inspect.getsource(remove_population_hdi_columns)
    assert "drop" in source_code, "df.drop() is not used in the function"

    # Create test DataFrame
    df = pd.DataFrame({
        'Population': [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
        'GDP': [
            1785387,
            2833687,
            3874437,
            2167744,
            4602367,
            2950039,
            17348075
        ],
        'Surface Area': [
            9984670,
            640679,
            357114,
            301336,
            377930,
            242495,
            9525067
        ],
        'HDI': [
            0.913,
            0.888,
            0.916,
            0.873,
            0.891,
            0.907,
            0.915
        ],
        'Continent': [
            'America',
            'Europe',
            'Europe',
            'Europe',
            'Asia',
            'Europe',
            'America'
        ]
    }, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

    # Apply function
    result = remove_population_hdi_columns(df)

    # Validate DataFrame structure
    assert isinstance(result, pd.DataFrame), "Function did not return a DataFrame"
    assert 'Population' not in result.columns, "'Population' column was not removed"
    assert 'HDI' not in result.columns, "'HDI' column was not removed"

    print("✅ Test Passed: remove_population_hdi_columns() is implemented correctly.")