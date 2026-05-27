"""
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
"""

import pandas as pd

tweets = {
    "tweet_id": [1, 2],
    "content": ["Vote for Biden", "Let us make America great again!"],
}

tweet_df = pd.DataFrame(tweets)


def invalid_tweets(tweets):
    # Filter and just get invalid tweets
    invalid_tweet_df = tweets[tweets["content"].str.len() > 15]

    results_df = invalid_tweet_df[["tweet_id"]]

    return results_df


print(invalid_tweets(tweets=tweet_df))
