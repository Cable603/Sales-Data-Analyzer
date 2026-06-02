"""
File: statistics.py

Description: 
Computes mathematical and statistical processes on data 
"""

import pandas as pd
import numpy as np


def calculate_mean(
    series: pd.Series
) -> float:
    pass


def calculate_median(
    series: pd.Series
) -> float:
    pass


def calculate_mode(
    series: pd.Series
) -> pd.Series:
    pass


def calculate_standard_deviation(
    series: pd.Series
) -> float:
    pass


def calculate_variance(
    series: pd.Series
) -> float:
    pass


def calculate_min(
    series: pd.Series
) -> float:
    pass


def calculate_max(
    series: pd.Series
) -> float:
    pass


def calculate_range(
    series: pd.Series
) -> float:
    pass


def calculate_percentile(
    series: pd.Series,
    percentile: float
) -> float:
    pass


def calculate_quartiles(
    series: pd.Series
) -> dict:
    pass


def calculate_iqr(
    series: pd.Series
) -> float:
    pass


def calculate_z_scores(
    series: pd.Series
) -> np.ndarray:
    pass


def detect_outliers_iqr(
    series: pd.Series
) -> pd.Series:
    pass


def detect_outliers_zscore(
    series: pd.Series,
    threshold: float = 3.0
) -> pd.Series:
    pass


def calculate_correlation(
    series_one: pd.Series,
    series_two: pd.Series
) -> float:
    pass


def calculate_covariance(
    series_one: pd.Series,
    series_two: pd.Series
) -> float:
    pass


def salary_distribution_statistics(
    df: pd.DataFrame
) -> dict:
    pass


def age_distribution_statistics(
    df: pd.DataFrame
) -> dict:
    pass


def bonus_distribution_statistics(
    df: pd.DataFrame
) -> dict:
    pass


def summarize_numeric_column(
    series: pd.Series
) -> dict:
    pass