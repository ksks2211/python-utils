import json
import logging as logger

import pandas as pd


def read_csv_as_df(filepath: str):
    return pd.read_csv(filepath, thousands=",")


def read_csv_as_dict_list(filepath: str):
    df = read_csv_as_df(filepath)
    return df.to_dict(orient="records")


def save_csv_to_json(origin_file: str, save_file: str, title: str = "records"):

    try:
        arr = read_csv_as_dict_list(origin_file)
        final_dict = {title: arr}
        with open(save_file, "w", encoding="utf-8") as file:
            json.dump(final_dict, file, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error("csv to json conversion failed!", e)
        return False
    return True
