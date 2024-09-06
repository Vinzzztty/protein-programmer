"""
Example 1:

Input: 
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
Explanation: 
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
"""

import pandas as pd

data = {
    "teacher_id": [1, 1, 1, 2, 2, 2, 2],
    "subject_id": [2, 2, 3, 1, 2, 3, 4],
    "dept_id": [3, 4, 3, 1, 1, 1, 1],
}

teacher_df = pd.DataFrame(data)


def count_unique_subjects(teachers):
    # Group by teacher_id and count the number of unique subject_ids
    result_df = teachers.groupby("teacher_id")["subject_id"].nunique().reset_index()

    result_df.rename(columns={"subject_id": "cnt"}, inplace=True)

    return result_df


print(count_unique_subjects(teacher_df))
