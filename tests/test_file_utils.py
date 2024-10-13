from python_utils.file_utils import write_file


def test_file_save():
    write_file("tmp/test.txt", "this is test text")
