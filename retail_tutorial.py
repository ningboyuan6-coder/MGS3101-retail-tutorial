import pandas as pd

pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda value: f'{value:,.2f}')
def demo_pandas_fundamentals():
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