import os
import sys
#from os import listdir, mkdir
#from os.path import isfile, join
#import json
from copy import deepcopy
import googleVisionOCR
import dataTemplate

# Add extraction module imports here
import dateExtraction
import rankExtraction


def extract(args):
    """Runs extraction scripts and returns data in a single dictionary"""
    # args is: 'full_path\\filename1.json full_path\\filename2.json'
    # filename2 is only present for uprights

    # access empty data template
    # deepcopy here since we do not want to modify the single empty_data dictionary
    record_data = deepcopy(dataTemplate.data_template)

    # Do not call any extraction scripts if args is empty
    if args:
        # BEGIN EXTRACTION CALLS
        # NOTE: order matters here if any extraction scripts have key overlap
        # NOTE: Extraction scripts should return key/value pairs (dictionary)
        # NOTE: Add additional extraction script calls here
        # FORMAT: record_data.update(<script_file_name.script_function_name>(args))
        record_data.update(dateExtraction.extract_dates(args))

        # END EXTRACTION CALLS
    return record_data


def setup_paths(file_path):
    """Set up Google Vision and tempFiles directories"""
    json_path = file_path + "\\GoogleVisionData\\"
    temp_path = file_path + "\\tempFiles\\"
    if not os.path.isdir(temp_path):
        os.mkdir(temp_path)
    return json_path, temp_path


def get_record_type_list(file_path):
    """Get data from recordTypeList and return list of file name pairs
       (for uprights) and single file names (for flats)"""
    record_type_list = []
    # Open "recordTypeList.tmp" file and read into list, strip to remove \n
    with open(file_path + "\\recordTypeList.tmp", 'r') as file:
        lines = file.readlines()
    lines = filter(lambda line: line.strip(), lines)  # removes any blank lines
    record_type_list = [line.strip() for line in lines]  # strips \n from end
    # recordTypeList is now a list containing the file name arguments to be
    # sent to each extraction module/script
    return record_type_list


def setup_args(file_list, json_path):
    """Returns argument list for extraction scripts"""
    arg_list = []
    file_path1 = file_path2 = ""
    if len(file_list) == 1:
        file_path1 = json_path + file_list[0] + ".json"
        arg_list.append(file_path1)
    elif len(file_list) == 2:
        file_path1 = json_path + file_list[0] + ".json"
        arg_list.append(file_path1)
        file_path2 = json_path + file_list[1] + ".json"
        arg_list.append(file_path2)

    # arg_list is: ['full_path\\filename1.json', 'full_path\\filename2.json']
    # filename2 is only present for uprights

    # pass arg_list to extraction modules
    args = ""
    if len(arg_list) == 1:
        args = arg_list[0]
    elif len(arg_list) == 2:
        args = arg_list[0] + " " + arg_list[1]
    # args is: 'full_path\\filename1.json full_path\\filename2.json'
    # filename2 is only present for uprights
    return args


def main(argv):
    # Get file path
    file_path = sys.argv[1]

    # Call Google Vision to create .json files in GoogleVisionData directory
    googleVisionOCR.OCR(file_path)

    # Set up paths
    json_path, temp_path = setup_paths(file_path)

    # grab list from file "recordTypeList.tmp"
    record_type_list = get_record_type_list(file_path)

    for line in record_type_list:
        # line is a string in this format: 'filename1' or 'filename1 filename2'
        # file_list is: ['filename1'] or ['filename1', 'filename2']
        file_list = line.split()

        # set up arguments for extraction scripts (file path/names)
        args = setup_args(file_list, json_path)

        # extract data / run extraction scripts
        record_data = extract(args)

        # write output record_data to .tmp files
        # only write the filename for the primary (for uprights)
        output_file_path = temp_path + file_list[0] + ".tmp"
        try:
            with open(output_file_path, "w+") as file:
                file.write("")
                for i in record_data:
                    file.write(i + ":" + record_data[i] + "\n")
        except IOError:
            print("Error writing to file: ", output_file_path)


if __name__ == "__main__":
    main(sys.argv)
