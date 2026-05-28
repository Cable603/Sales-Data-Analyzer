"""
File: cleaner.py

Description:
cleans loaded files 
"""

import pandas as pd
from datetime import datetime


def remove_duplicates(df:pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate employee records based on EEID.
    """
    return df.drop_duplicates(subset=["EEID"])


def handle_missing_values(df:pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values safely.
    """

    # Remove rows missing critical salary data
    df = df.dropna(subset=["Annual Salary"])

    # Fill missing bonus percentages with 0
    df["Bonus %"] = df["Bonus %"].fillna(0)

    # Fill missing text fields with 'Unknown'
    text_columns = [
        "Gender",
        "Ethnicity",
        "Department",
        "Job Title",
        "Business Unit",
        "Country",
        "City"
    ]

    for col in text_columns:
        df[col] = df[col].fillna("Unknown")

    return df


def convert_numeric_columns(df:pd.DataFrame) -> pd.DataFrame:
    """
    Convert numeric columns to proper numeric types.
    """

    numeric_columns = [
        "Annual Salary",
        "Bonus %",
        "Age"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def convert_date_columns(df:pd.DataFrame) -> pd.DataFrame:
    """
    Convert date columns into datetime objects.
    """

    date_columns = [
        "Hire Date",
        "Exit Date"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def normalize_text_columns(df:pd.DataFrame) -> pd.DataFrame:
    """
    Normalize formatting for text-based columns.
    """

    text_columns = [
        "Gender",
        "Ethnicity",
        "Department",
        "Job Title",
        "Business Unit",
        "Country",
        "City"
    ]

    for col in text_columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

    return df


def remove_invalid_rows(df:pd.DataFrame) -> pd.DataFrame:
    """
    Remove logically invalid records.
    """

    # Remove negative or zero salaries
    df = df[df["Annual Salary"] > 0]

    # Remove impossible ages
    df = df[(df["Age"] >= 16) & (df["Age"] <= 100)]

    # Remove impossible bonus percentages
    df = df[(df["Bonus %"] >= 0) & (df["Bonus %"] <= 100)]

    return df


def create_derived_columns(df:pd.DataFrame) -> pd.DataFrame:
    """
    Create useful derived columns for analysis.
    """

    current_year = datetime.now().year

    # Employee tenure
    df["Tenure"] = (
        current_year - df["Hire Date"].dt.year
    )

    # Whether employee is still active
    df["Is Active"] = df["Exit Date"].isna()

    # Total compensation
    df["Total Compensation"] = (
        df["Annual Salary"] +
        (df["Annual Salary"] * (df["Bonus %"] / 100))
    )

    return df


def clean_dataset(df:pd.DataFrame) -> pd.DataFrame:
    """
    Master cleaning pipeline.
    """

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = convert_numeric_columns(df)

    df = convert_date_columns(df)

    df = normalize_text_columns(df)

    df = remove_invalid_rows(df)

    df = create_derived_columns(df)

    return df