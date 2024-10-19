import logging as logger

from python_utils.array_utils import divide_by_bins, percentile


def test_percentile():

    ages = [10, 50, 20, 55, 22, 6, 16, 83, 66, 3, 100]
    median = percentile(ages, 50.0)

    n = len(ages) // 2
    ages.sort()

    logger.info(f"median age is {median}")

    assert ages[n] == median


def test_divider():
    ages = [10, 50, 20, 55, 22, 6, 16, 83, 66, 3, 100]
    bins = [0, 20, 40, 60, 80, 100]
    cat = divide_by_bins(ages, bins)

    logger.info(f"{cat}")

    # 각각이 속한 카테고리 번호
    logger.info(f"{cat.codes}")

    # 각 카테고리별 범위
    logger.info(f"{cat.categories}")
