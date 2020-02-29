import sys
sys.path.append("C:/Python/FourFrontScripts")
import os
import controller


def test_setup_paths_json_name():
    # test normal file path with no spaces
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\test_dir'
    json = file_path + '\\GoogleVisionData\\'
    temp = file_path + '\\tempFiles\\'
    test_json, test_temp = controller.setup_paths(file_path)
    assert test_json == json
    os.rmdir(test_temp)


def test_setup_paths_temp_name():
    # test normal file path with no spaces
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\test_dir'
    json = file_path + '\\GoogleVisionData\\'
    temp = file_path + '\\tempFiles\\'
    test_json, test_temp = controller.setup_paths(file_path)
    assert test_temp == temp
    os.rmdir(test_temp)


def test_setup_paths():
    # test normal file path with no spaces
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\test_dir'
    json = file_path + '\\GoogleVisionData\\'
    temp = file_path + '\\tempFiles\\'
    test_json, test_temp = controller.setup_paths(file_path)
    assert os.path.exists(test_temp)
    os.rmdir(test_temp)


def test_setup_paths_json_name_with_spaces():
    # test file path with spaces
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\test dir spaces'
    json = file_path + '\\GoogleVisionData\\'
    temp = file_path + '\\tempFiles\\'
    test_json, test_temp = controller.setup_paths(file_path)
    assert test_json == json
    os.rmdir(test_temp)


def test_setup_paths_temp_name_with_spaces():
    # test file path with spaces
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\test dir spaces'
    json = file_path + '\\GoogleVisionData\\'
    temp = file_path + '\\tempFiles\\'
    test_json, test_temp = controller.setup_paths(file_path)
    assert test_temp == temp
    os.rmdir(test_temp)


def test_setup_paths_with_spaces():
    # test file path with spaces
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\test dir spaces'
    json = file_path + '\\GoogleVisionData\\'
    temp = file_path + '\\tempFiles\\'
    test_json, test_temp = controller.setup_paths(file_path)
    assert os.path.exists(test_temp)
    os.rmdir(test_temp)


def test_get_record_type_list1():
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\recordTypeLists\\1'
    record_type_list = ['2019-06-14_08-43-57_002',
                        '2019-06-14_08-44-33_003',
                        '2019-06-14_08-47-45_005',
                        '2019-06-14_08-48-03_006',
                        '2019-06-14_08-48-11_007']
    test_list = controller.get_record_type_list(file_path)
    assert test_list == record_type_list


def test_get_record_type_list2():
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\recordTypeLists\\2'
    record_type_list = ['2019-11-05_13-51-28_083 2019-11-05_13-51-35_085',
                        '2019-11-05_13-51-42_086 2019-11-05_13-51-47_087',
                        '2019-11-05_13-51-53_087 2019-11-05_13-51-58_088',
                        '2019-11-05_13-52-06_090 2019-11-05_13-52-13_091',
                        '2019-11-05_13-52-18_091 2019-11-05_13-52-24_093']
    test_list = controller.get_record_type_list(file_path)
    assert test_list == record_type_list


def test_get_record_type_list_mixed():
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\recordTypeLists\\mixed'
    record_type_list = ['2019-06-14_08-43-57_002',
                        '2019-06-14_08-44-33_003',
                        '2019-06-14_08-47-45_005',
                        '2019-06-14_08-48-03_006',
                        '2019-06-14_08-48-11_007',
                        '2019-11-05_13-51-28_083 2019-11-05_13-51-35_085',
                        '2019-11-05_13-51-42_086 2019-11-05_13-51-47_087',
                        '2019-11-05_13-51-53_087 2019-11-05_13-51-58_088',
                        '2019-11-05_13-52-06_090 2019-11-05_13-52-13_091',
                        '2019-11-05_13-52-18_091 2019-11-05_13-52-24_093',
                        '2019-06-14_08-48-19_008',
                        '2019-06-14_08-48-28_008',
                        '2019-06-14_08-48-36_010',
                        '2019-06-14_08-49-07_011',
                        '2019-06-14_08-49-13_012',
                        '2019-11-05_13-52-31_093 2019-11-05_13-52-36_094',
                        '2019-11-05_13-52-43_095 2019-11-05_13-52-49_095',
                        '2019-11-05_13-53-23_098 2019-11-05_13-53-31_099',
                        '2019-11-05_13-53-37_100 2019-11-05_13-53-42_101',
                        '2019-11-05_13-53-48_102 2019-11-05_13-53-54_103',
                        '2019-06-14_08-49-22_013',
                        '2019-06-14_08-49-30_014',
                        '2019-06-14_08-49-37_015',
                        '2019-06-14_08-49-43_015',
                        '2019-06-14_08-49-51_016',
                        '2019-06-14_08-50-19_018',
                        '2019-06-14_08-50-27_019',
                        '2019-06-14_08-50-36_020',
                        '2019-06-14_08-50-43_021',
                        '2019-06-14_08-50-51_022',
                        '2019-06-14_08-50-58_023',
                        '2019-06-14_08-51-05_024',
                        '2019-06-14_08-51-13_024',
                        '2019-06-14_08-51-20_026',
                        '2019-06-14_08-51-39_027']
    test_list = controller.get_record_type_list(file_path)
    assert test_list == record_type_list


def test_get_record_type_list_blank_lines():
    file_path = 'C:\\Python\\FourFrontScripts\\tests\\resources\\recordTypeLists\\blank_lines'
    record_type_list = ['2019-06-14_08-43-57_002',
                        '2019-06-14_08-44-33_003',
                        '2019-06-14_08-47-45_005',
                        '2019-06-14_08-48-03_006',
                        '2019-06-14_08-48-11_007']
    test_list = controller.get_record_type_list(file_path)
    assert test_list == record_type_list


def test_setup_args():
    file_list = ['one', 'two']
    json_path = 'some_path\\'
    args = 'some_path\\one.json some_path\\two.json'
    test_args = controller.setup_args(file_list, json_path)
    assert test_args == args


def test_setup_args_spaces():
    file_list = ['one file', 'two file']
    json_path = 'some_path\\'
    args = 'some_path\\one file.json some_path\\two file.json'
    test_args = controller.setup_args(file_list, json_path)
    assert test_args == args

