import logging as logger

from python_utils.api_utils import s3_client
from tests.helper import get_env


def test_list_files():
    bucket = get_env("S3_BUCKET_NAME")
    assert bucket is not None

    prefix = "dist/"

    try:
        files = s3_client.list(bucket, prefix)
        for file in files:
            logger.info(f"File: {file['Key']}")
    except Exception as e:
        logger.error("Unexpected error", e)


def test_upload_file():
    filename = "tmp/test.txt"
    bucket = get_env("S3_BUCKET_NAME")
    assert bucket is not None

    key = "test2.txt"

    try:
        s3_client.upload(filename, bucket, key)
        logger.info("File uploaded successfully!")
    except FileNotFoundError as fnfe:
        logger.error("File not found", fnfe)
    except s3_client.FileUploadError as fue:
        logger.error("File upload failed", fue)
    except Exception as e:
        logger.error("Unexpected error", e)
