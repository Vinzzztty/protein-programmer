"""
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

"""

import pandas as pd

viewers = {
    "article_id": [1, 1, 2, 2, 4, 3, 3],
    "author_id": [3, 3, 7, 7, 7, 4, 4],
    "viewer_id": [5, 6, 7, 6, 1, 4, 4],
    "view_date": [
        "2019-08-01",
        "2019-08-02",
        "2019-08-01",
        "2019-08-02",
        "2019-07-22",
        "2019-07-21",
        "2019-07-21",
    ],
}

viewer_df = pd.DataFrame(viewers)


def article_views(views):
    # Filter value column with a same id in column author_id, and viewer_id
    author_read_article = views[views["author_id"] == views["viewer_id"]]

    # Get unique author_ids from the filtered data
    unique_authors = author_read_article["author_id"].unique()

    # Sort by ascending order
    unique_authors = sorted(unique_authors)

    result_df = pd.DataFrame({"id": unique_authors})

    return result_df


print(article_views(views=viewer_df))
