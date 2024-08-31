"""
Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
Output: 
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
Explanation: 
Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.
"""

import pandas as pd

data = {
    "emp_id": [1, 1, 1, 2, 2],
    "event_day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"],
    "in_time": [4, 55, 1, 3, 47],
    "out_time": [32, 200, 42, 33, 74],
}

employee_df = pd.DataFrame(data)


def total_time(employees):
    # Menghitung the time spent for each entry
    employees["total_time"] = employees["out_time"] - employees["in_time"]

    # Group by emp_id and event_day to sum the total_time
    result = (
        employees.groupby(["emp_id", "event_day"])["total_time"].sum().reset_index()
    )

    result.rename(columns={"event_day": "day"}, inplace=True)

    return result[["day", "emp_id", "total_time"]]


print(total_time(employee_df))
