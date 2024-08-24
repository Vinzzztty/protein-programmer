"""
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
"""

import pandas as pd

data = {
    "student_id": [101, 53, 128, 3],
    "name": ["Ulysses", "William", "Henry", "Henry"],
    "age": [13, 10, 6, 11],
}

student_df = pd.DataFrame(data=data)


def selectData(students):
    select_student = students[students["student_id"] == 101]

    return select_student[["name", "age"]]


print(selectData(student_df))
