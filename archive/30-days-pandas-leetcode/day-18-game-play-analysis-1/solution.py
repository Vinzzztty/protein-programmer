"""
Write a solution to find the first login date for each player.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
"""

import pandas as pd

data = {
    "player_id": [1, 1, 2, 3, 3],
    "device_id": [2, 2, 3, 1, 4],
    "event_date": [
        "2016-03-01",
        "2016-05-02",
        "2017-06-25",
        "2016-03-02",
        "2018-07-03",
    ],
    "games_played": [5, 6, 1, 0, 5],
}

activity_df = pd.DataFrame(data)


def game_analysis(activity):
    first_login_df = activity.groupby("player_id")["event_date"].agg(min).reset_index()

    result_df = first_login_df.rename(columns={"event_date": "first_login"})

    return result_df


print(game_analysis(activity_df))
