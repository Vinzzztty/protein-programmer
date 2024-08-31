"""
The result format is in the following example.

Example 1:
Input:
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
Output:
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
Explanation: 
The column names are changed accordingly.
"""

import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "first": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
    "last": ["King", "Wright", "Hall", "Thompson", "Moore"],
    "age": [6, 7, 16, 18, 10],
}

student_df = pd.DataFrame(data)


def renameColumns(students):
    result_df = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )

    return result_df


print(renameColumns(student_df))
