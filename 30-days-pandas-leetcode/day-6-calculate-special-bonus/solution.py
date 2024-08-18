"""
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 

Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

EXAMPLE
Input: 
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
Output: 
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
Explanation: 
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.
"""

import pandas as pd

employee = {
    "employee_id": [2, 3, 7, 8, 9],
    "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
    "salary": [3000, 3800, 7400, 6100, 7700],
}

employees_df = pd.DataFrame(employee)


def calculate_special_bonus(employees):
    # initialize bonus to 0 for all employees
    employees["bonus"] = 0

    # filter employee_id with an odd employee_id
    odd_employeeId = employees[employees["employee_id"] % 2 != 0]

    # filter name whose names do not start with 'M'
    eligible_employee = odd_employeeId[~odd_employeeId["name"].str.startswith("M")]

    # print(eligible_employee)

    # Assign a 100% bonus (same as their salary) to eligible employees
    employees.loc[eligible_employee.index, "bonus"] = eligible_employee["salary"]

    # sort the result by employee_id
    sorted_employees = employees[["employee_id", "bonus"]].sort_values(
        by="employee_id", ascending=True
    )

    return sorted_employees


print(calculate_special_bonus(employees=employees_df))
