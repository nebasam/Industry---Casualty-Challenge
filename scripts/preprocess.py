import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from logger import logger

def check_numeric(df: pd.DataFrame) -> list:
    """[summary]
    Args:
        df (pd.DataFrame): Dataframe to be checked for non-numeric value
    Returns:
        struct_data (pd.DataFrame): Copied DataFrame
        non_numeric columns (list): Returns list of non numeric columns
    """
    struct_data = df.copy()
 
    non_numeric_columns = list(struct_data.select_dtypes(exclude=[np.number]).columns)
    print(non_numeric_columns)
    return struct_data, non_numeric_columns


def label_encode(df: pd.DataFrame, non_numeric_columns: list) -> pd.DataFrame:
    """Label encodes DataFrame
    Args:
        struct_data (pd.DataFrame): DataFrame to be encoded
        non_numeric_columns (list): list containing the numeric columns in DataFrame
    Returns:
        pd.DataFrame: Label encoded DataFrame
    """
    try:
        le = LabelEncoder()
        for col in non_numeric_columns:
            df[col] = le.fit_transform(df[col])
        logger.info(f'encodes label for non_numeric successfully')
        return df
    except Exception:
        logger.exception('encodeing label for non_numeric failed.')
        
def scale():
    # TODO do scaling functionality
    pass