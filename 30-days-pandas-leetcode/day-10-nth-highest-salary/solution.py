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
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

E X A M P L E

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

"""

import pandas as pd

data = {"id": [1, 2, 3], "salary": [100, 200, 300]}

n = 2

employee_df = pd.DataFrame(data)


def nth_highest_salary(emplyee, N):

    # Drop duplikat salary
    unique_salaries = emplyee["salary"].drop_duplicates()

    # sort unique salaries descending
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # If there is no nth highest salary, return null
    if N > len(sorted_salaries) or N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    # GET the Nth highest salary
    nth_highest = sorted_salaries.iloc[N - 1]

    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_highest]})


print(nth_highest_salary(employee_df, n))
