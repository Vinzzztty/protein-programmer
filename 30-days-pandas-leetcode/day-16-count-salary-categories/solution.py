"""
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output: 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation: 
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
"""

import pandas as pd

data = {"account_id": [3, 2, 8, 6], "income": [108939, 12747, 87709, 91796]}

account_df = pd.DataFrame(data)


def count_salary_categories(accounts):
    return pd.DataFrame(
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "account_count": [
                accounts[accounts.income < 20000].shape[0],
                accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[
                    0
                ],
                accounts[accounts.income > 50000].shape[0],
            ],
        }
    )


print(count_salary_categories(account_df))
