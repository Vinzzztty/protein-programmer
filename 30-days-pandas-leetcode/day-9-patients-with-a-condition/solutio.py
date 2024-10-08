"""
Table: Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
 

Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

EXAMPLE
Input: 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
Output: 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+
Explanation: Bob and George both have a condition that starts with DIAB1.
"""

import pandas as pd

patient = {
    "patient_id": [1, 2, 3, 4, 5],
    "patient_name": ["Daniel", "Alice", "Bob", "George", "Alain"],
    "conditions": ["YFEV COUGH", "", "DIAB100 MYOP", "ACNE DIAB100", "DIAB201"],
}

patient_df = pd.DataFrame(patient)


def find_patients(patiens):

    patient_diabetes = patiens[patiens["conditions"].str.contains(r"\bDIAB1")]

    return patient_diabetes


print(find_patients(patient_df))
