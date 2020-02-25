import pytest
import dateExtraction


def test_args_to_file_list1():
    """parse_args_to_file_list should return list of single file name"""
    file1 = "C:\\SomeSection\\GoogleVisionData\\some_file.json"
    args = (file1, )
    files = dateExtraction.parse_args_to_file_list(args)
    file_list = list()
    file_list.append(file1)
    assert files == file_list


def test_args_to_file_list2():
    """parse_args_to_file_list should return list of file names"""
    file1 = "C:\\SomeSection\\GoogleVisionData\\some_file1.json"
    file2 = "C:\\SomeSection\\GoogleVisionData\\some_file2.json"
    args = (file1 + " " + file2, )
    files = dateExtraction.parse_args_to_file_list(args)
    file_list = list()
    file_list.append(file1)
    file_list.append(file2)
    assert files == file_list


