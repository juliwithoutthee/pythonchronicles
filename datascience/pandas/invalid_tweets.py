import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """ Filter rows where the length of 'content' is greater than 15 characters. Then select 'tweet_id' column from the filtered DataFrame"""
    filtered_df = tweets[tweets['content'].str.len() > 15]
    result = filtered_df[['tweet_id']]
    return result