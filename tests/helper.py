import os

from dotenv import load_dotenv

# .env 파일을 로드
load_dotenv()


def get_env(key: str):
    return os.getenv(key)
