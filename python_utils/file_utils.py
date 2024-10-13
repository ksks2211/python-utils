from pathlib import Path


def write_file(file_path: str, content: str) -> None:
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(content)


def file_exists(file_path: str) -> bool:
    return Path(file_path).exists()
