"""
Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.

Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

Example 1:

Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

"""

import pandas as pd

data = {"id": [1, 2, 3, 4, 5, 6], "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]}

score_df = pd.DataFrame(data)


def order_scores(scores):
    # Use rank method to assign ranks to the scores in descending order with no gaps
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)

    # Drop id column, and sort with descending
    result_df = scores.drop("id", axis=1).sort_values(by="score", ascending=False)

    return result_df


print(order_scores(score_df))
