import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # where referee_id is not equal to 2 or is null
    filtered_df = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())]
    
    # select 'name' column from the filtered DataFrame
    result = filtered_df[['name']]
    
    return result