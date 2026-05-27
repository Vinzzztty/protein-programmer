"""
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

 

Example 1:
Input:
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Output:  
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
"""

import pandas as pd

data = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    "email": [
        "emily@example.com",
        "michael@example.com",
        "sarah@example.com",
        "john@example.com",
        "john@example.com",
        "alice@example.com",
    ],
}

customer_df = pd.DataFrame(data)


def dropDuplicatesEmail(customers):
    result_df = customers.drop_duplicates(subset="email", keep="first")

    return result_df


print(dropDuplicatesEmail(customer_df))
