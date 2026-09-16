import pandas as pd

pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda value: f'{value:,.2f}')
def demo_pandas_fundamentals():
    def load_and_inspect_data():
    print('\n--- Load and inspect retail data ---')

    retail_2009_10 = pd.read_csv('Retail 2009-10.csv')
    retail_2010_11 = pd.read_csv('Retail 2010-11.csv')

    print('2009-10 rows:', len(retail_2009_10))
    print('2010-11 rows:', len(retail_2010_11))

    print('\nColumns:')
    print(retail_2009_10.columns.tolist())

    print('\nFirst five rows:')
    print(retail_2009_10.head())

    print('\nMissing Customer ID:')
    print('2009-10:', retail_2009_10['Customer ID'].isna().sum())
    print('2010-11:', retail_2010_11['Customer ID'].isna().sum())

    return retail_2009_10, retail_2010_11
    print('\n--- Pandas fundamentals ---')

    series = pd.Series(
        [120, 85, 150],
        index=['Mon', 'Tue', 'Wed'],
        name='Units'
    )
    print('Series:')
    print(series)
    print('Tuesday units:', series.loc['Tue'])

    data = {
        'Product': ['Notebook', 'Pen', 'Backpack'],
        'Units': [120, 85, 150],
        'Price': [4.50, 1.75, 32.00],
    }
    df = pd.DataFrame(data)
    df['Revenue'] = df['Units'] * df['Price']

    print('\nDataFrame:')
    print(df)
    print('\nSummary statistics:')
    print(df.describe())
    def load_and_inspect_data():
    print('\n--- Load and inspect retail data ---')

    retail_2009_10 = pd.read_csv('Retail 2009-10.csv')
    retail_2010_11 = pd.read_csv('Retail 2010-11.csv')

    print('2009-10 rows:', len(retail_2009_10))
    print('2010-11 rows:', len(retail_2010_11))

    print('\nColumns:')
    print(retail_2009_10.columns.tolist())

    print('\nFirst five rows:')
    print(retail_2009_10.head())

    print('\nMissing Customer ID:')
    print('2009-10:', retail_2009_10['Customer ID'].isna().sum())
    print('2010-11:', retail_2010_11['Customer ID'].isna().sum())

    return retail_2009_10, retail_2010_11