import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    result = filtered_df[['product_id']]
    return result

'''
note:
When returning a DataFrame, use double square brackets [[]] to select the column. This ensures that the result is a DataFrame with a single column instead of a Series.
'''