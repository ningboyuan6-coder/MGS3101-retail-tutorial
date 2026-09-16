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


def clean_and_prepare_data(retail_2009_10, retail_2010_11):
    print('\n--- Clean and prepare data ---')

    retail = pd.concat(
        [retail_2009_10, retail_2010_11],
        ignore_index=True
    )

    retail.columns = (
        retail.columns
        .str.strip()
        .str.replace(' ', '_')
    )

    retail['InvoiceDate'] = pd.to_datetime(
    retail['InvoiceDate'],
    dayfirst=True
)

    retail['Is_Cancelled'] = (
        retail['Invoice'].astype(str).str.startswith('C')
    )

    print('Combined raw rows:', len(retail))
    print('Cancellation/return rows:', retail['Is_Cancelled'].sum())

    retail = retail[
        (~retail['Is_Cancelled'])
        & (retail['Quantity'] > 0)
        & (retail['Price'] > 0)
    ].copy()

    retail['Is_Registered'] = retail['Customer_ID'].notna()

    retail['Revenue'] = retail['Quantity'] * retail['Price']

    print('Valid completed sales:', len(retail))
    print('Net revenue:', retail['Revenue'].sum())

    return retail


def make_recommendations(retail):
    print('\n--- Recommendations ---')

    country_revenue = (
        retail.groupby('Country')['Revenue']
        .sum()
        .sort_values(ascending=False)
    )

    product_revenue = (
        retail.groupby('Description')['Revenue']
        .sum()
        .sort_values(ascending=False)
    )

    registered_revenue = (
        retail.groupby('Is_Registered')['Revenue']
        .sum()
    )

    print(
        'Recommendation 1: Focus marketing on the highest-revenue countries.'
    )
    print(country_revenue.head(5))

    print(
        '\nRecommendation 2: Prioritize the highest-revenue products.'
    )
    print(product_revenue.head(10))

    print(
        '\nRecommendation 3: Compare registered vs. unregistered customer revenue.'
    )
    print(registered_revenue)


def main():
    demo_pandas_fundamentals()

    retail_2009_10, retail_2010_11 = load_and_inspect_data()

    retail = clean_and_prepare_data(
        retail_2009_10,
        retail_2010_11
    )

    make_recommendations(retail)


if __name__ == '__main__':
    main()