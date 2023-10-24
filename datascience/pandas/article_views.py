import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filtering rows where author_id equals viewer_id
    filtered_df = views[views['author_id'] == views['viewer_id']]

    # Selecting 'author_id' column and dropping duplicates
    # Sort id by ascending order
    result = filtered_df[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'}).sort_values(by='id', ascending=True)

    return result

"""
SQL
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;

"""