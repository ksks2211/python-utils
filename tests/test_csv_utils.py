import logging as logger

from python_utils.csv_utils import (
    read_csv_as_df,
    read_csv_as_dict_list,
    save_csv_to_json,
)


def test_read_csv_as_df():
    filepath = "tmp/seoul.csv"
    df = read_csv_as_df(filepath)
    logger.info(df.index)
    logger.info(df)
    logger.info(df.columns)


def test_read_csv_as_dict_list():
    filepath = "tmp/seoul.csv"
    arr = read_csv_as_dict_list(filepath)
    logger.info(arr)


def test_save_csv_to_json():

    city = "tokyo"
    file_path = f"tmp/{city}.csv"
    save_path = f"tmp/{city}.json"
    save_csv_to_json(file_path, save_path, "demographics")
