import yaml


def save_dict_as_yaml(data: dict, filename: str) -> None:
    with open(filename, "w") as file:
        yaml.safe_dump(data, file)


def read_yaml_as_dict(filename: str) -> None | dict:

    with open(filename, "r") as file:
        return yaml.safe_load(file)
    return None
