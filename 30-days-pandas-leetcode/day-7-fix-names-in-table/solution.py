"""
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

EXAMPLE
Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
"""

import pandas as pd

user = {"user_id": [1, 2], "name": ["aLIce", "bOB"]}

user_df = pd.DataFrame(user)


def fix_names(users):

    # Fix values in column name
    users["name"] = users["name"].str.capitalize()

    # Sort ascending by user_id
    sorted_users = users.sort_values(by="user_id", ascending=True)

    return sorted_users


print(fix_names(users=user_df))
