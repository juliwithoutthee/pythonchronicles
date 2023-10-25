import pandas as pd

"""
SELECT COALESCE(eu.unique_id, NULL) AS unique_id, 
       e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;
"""

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join on 'id' column between employees and employee_uni DataFrames
    pass