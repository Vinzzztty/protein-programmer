"""
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""

import pandas as pd

data = {"id": [1, 2, 3], "salary": [100, 200, 300]}

employee_df = pd.DataFrame(data=data)


def second_highest_salary(employees):
    # Drop duplikat salary
    unique_salaries = employees["salary"].drop_duplicates().sort_values(ascending=False)

    if len(unique_salaries) == 1:
        return pd.DataFrame([{"SecondHighestSalary": None}])

    # Calculate the second highest salary
    second_highest = unique_salaries.iloc[1]

    result_df = pd.DataFrame({"SecondHighestSalary": [second_highest]})

    return result_df


print(second_highest_salary(employee_df))
