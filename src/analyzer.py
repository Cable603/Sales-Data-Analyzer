"""
File: analyzer.py

Description:
Groups mathematical analysis by dataset info 
"""

import pandas as pd
import statistics

def salary_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns total sum of salaries in the department
    """
    return df.groupby("Department", as_index=False)["Salary"].sum()

def salary_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Gender", as_index=False)["Salary"].sum()


def salary_by_ethnicity(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Ethnicity", as_index=False)["Salary"].sum()


def salary_by_country(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Country", as_index=False)["Salary"].sum()


def salary_by_job_title(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Job Title", as_index=False)["Salary"].sum()


def average_salary(df: pd.DataFrame) -> float:
    return statistics.calculate_mean(df["Salary"])


def median_salary(df: pd.DataFrame) -> float:
    return statistics.calculate_median(df["Salary"])


def highest_paid_employees(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    result = df.sort_values("Salary", ascending=False)
    return result.head(n=top_n)
        


def lowest_paid_employees(df: pd.DataFrame,bottom_n: int = 10) -> pd.DataFrame:
    result = df.sort_values("Salary", ascending=True)
    return result.head(n=bottom_n)

def department_employee_counts(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Department").size()


def active_vs_inactive_counts(df: pd.DataFrame) -> dict:
    result = {
        "Active":0,
        "Inactive":0
    }
    for row in df.itertuples():
        if row.Exit_Date == NONE:
            result["Inactive"]+= 1
        else:
            result["Active"]+= 1


def turnover_by_department(df: pd.DataFrame) -> pd.DataFrame:
    pass


def turnover_by_country(df: pd.DataFrame) -> pd.DataFrame:
    pass


def average_tenure(df: pd.DataFrame) -> float:
    pass


def tenure_by_department(df: pd.DataFrame) -> pd.DataFrame:
    pass


def hires_per_year(df: pd.DataFrame) -> pd.DataFrame:
    pass


def exits_per_year(df: pd.DataFrame) -> pd.DataFrame:
    pass


def bonus_by_department(df: pd.DataFrame) -> pd.DataFrame:
    pass


def total_compensation_by_department(df: pd.DataFrame) -> pd.DataFrame:
    pass


def age_distribution(df: pd.DataFrame) -> pd.Series:
    pass


def gender_distribution(df: pd.DataFrame) -> pd.Series:
    pass


def ethnicity_distribution(df: pd.DataFrame) -> pd.Series:
    pass


def country_distribution(df: pd.DataFrame) -> pd.Series:
    pass


def correlation_salary_tenure(df: pd.DataFrame) -> float:
    pass


def correlation_salary_age(df: pd.DataFrame) -> float:
    pass


def employees_above_salary(df: pd.DataFrame,threshold: float) -> pd.DataFrame:
    pass


def employees_below_salary(df: pd.DataFrame,threshold: float) -> pd.DataFrame:
    pass


def employees_by_department(df: pd.DataFrame,department: str) -> pd.DataFrame:
    pass


def employees_by_country(df: pd.DataFrame,country: str) -> pd.DataFrame:
    pass


def generate_summary_metrics(df: pd.DataFrame) -> dict:
    pass
