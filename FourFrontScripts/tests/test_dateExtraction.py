import pytest
import dateExtraction
import json


def test_args_to_file_list1():
    """parse_args_to_file_list should return list of single file name"""
    file1 = "C:\\SomeSection\\GoogleVisionData\\some_file.json"
    args = (file1, )
    files = dateExtraction.args_to_file_list(args)
    file_list = list()
    file_list.append(file1)
    assert files == file_list


def test_args_to_file_list2():
    """parse_args_to_file_list should return list of file names"""
    file1 = "C:\\SomeSection\\GoogleVisionData\\some_file1.json"
    file2 = "C:\\SomeSection\\GoogleVisionData\\some_file2.json"
    args = (file1 + " " + file2, )
    files = dateExtraction.args_to_file_list(args)
    file_list = list()
    file_list.append(file1)
    file_list.append(file2)
    assert files == file_list

### TODO(jd): Need tests for get_json_data function

### TODO(jd): Need tests for get_text_annotations function

### TODO(jd): Need tests for merge_text function

### TODO(jd): Need tests for parse_regex_dates function

### TODO(jd): Need tests for populate_output_dict function

### TODO(jd): Need tests for update_date_order function


