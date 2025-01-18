import boto3

from ..file_utils import file_exists


class FileUploadError(Exception):
    """Custom exception for file upload errors."""


s3_client = boto3.client("s3")


def upload(filename: str, bucket: str, key: str) -> None:
    """_summary_

    Args:
        filename (str): Path to the file up upload.
        bucket (str): S3 Bucket name
        key (str): S3 Object key

    Raises:
        FileNotFoundError: If the file does not exist.
        FileUploadError: If the upload to S3 fails.
    """

    if not file_exists(filename):
        raise FileNotFoundError(f"The file at {filename} does not exist.")
    try:
        s3_client.upload_file(filename, bucket, key)
    except Exception as e:
        raise FileUploadError(f"Failed to upload the file: {e}")


def list(bucket: str, prefix: str) -> list:
    """_summary_

    Args:
        bucket (str): S3 Bucket name
        prefix (str): Prefix to filter the objects in the bucket

    Returns:
        list: List of objects in the bucket with the given prefix
    """
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    return response.get("Contents", [])
