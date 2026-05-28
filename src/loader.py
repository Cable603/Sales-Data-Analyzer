"""
File: Loader.py

Description:
Loads in CSV or EXCEL file containing data 
"""

import pandas as pd

def csv_to_df(path:str) -> pd.DataFrame:
    return pd.read_csv(
        path,
        encoding="latin1"
    ) 
    
def excel_to_df(path:str) -> pd.DataFrame:
    return pd.read_excel(
        path
    )

