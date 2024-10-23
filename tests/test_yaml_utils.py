import logging as logger

from python_utils.yaml_utils import read_yaml_as_dict, save_dict_as_yaml


def test_yaml_read():

    filename = "tmp/example.yaml"

    data = read_yaml_as_dict(filename)

    logger.info(data)


def test_yaml_write():

    data = {"name": "jamie", "age": 100, "children": ["john", "tim", "mike", "brad"]}
    filename = "tmp/example2.yaml"

    save_dict_as_yaml(data, filename)
