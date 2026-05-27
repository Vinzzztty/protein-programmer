"""
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.

Write a solution to find employees who have the highest salary in each of the departments.

OUTPUT
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
"""

import pandas as pd

data_employee = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
    "salary": [70000, 90000, 80000, 60000, 90000],
    "departmentId": [1, 1, 2, 2, 1],
}

data_department = {"id": [1, 2], "name": ["IT", "Sales"]}

employee = pd.DataFrame(data_employee)
department = pd.DataFrame(data_department)


def department_highest_salary(employees, departments):

    # Merge dataframe
    merge_df = pd.merge(
        employees, departments, left_on="departmentId", right_on="id", how="left"
    )

    # Filter rows where salary matches the maximum salary within each department
    highest_salary = merge_df[
        merge_df["salary"] == merge_df.groupby("name_y")["salary"].transform("max")
    ]

    # Rename columns to output format
    result_df = highest_salary[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )

    return result_df


print(department_highest_salary(employee, department))
