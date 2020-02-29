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


def main(argv):
    # Get file path
    file_path = sys.argv[1]

    googleVisionOCR.OCR(file_path)
    
    json_path = file_path + "\\GoogleVisionData\\"
    temp_path = file_path + "\\tempFiles\\"
    if not os.path.isdir(temp_path):
        os.mkdir(temp_path)

    empty_data = dataTemplate.data_template
    
    # Open "recordTypeList.tmp" file and read into list, strip at ends
    record_type_list = []
    with open(file_path + "\\recordTypeList.tmp", 'r') as file:
        record_type_list = file.readlines()
    record_type_list = [line.strip() for line in record_type_list]
    # recordTypeList is now a list containing the arguments to be sent to each
    # extraction module/script

    for line in record_type_list:
        print(line)
        record_data = deepcopy(empty_data)

        # set up file path/names
        file_path1 = file_path2 = ""
        file_list = line.split()

        # set up arguments (file path/names)
        arg_list = []
        if len(file_list) == 1:
            file_path1 = json_path + file_list[0] + ".json"
            arg_list.append(file_path1)
        if len(file_list) == 2:
            file_path1 = json_path + file_list[0] + ".json"
            arg_list.append(file_path1)
            file_path2 = json_path + file_list[1] + ".json"
            arg_list.append(file_path2)
        
        # pass arg_list to extraction modules
        args = ""
        if len(arg_list) == 1:
            args = arg_list[0]
        elif len(arg_list) == 2:
            args = arg_list[0] + " " + arg_list[1]

        # call extraction modules
        dates = dateExtraction.extract_dates(args)
        # add more calls to extraction modules here

        # fill record_data
        for d in dates:
            record_data[d] = dates[d]
        # add more extraction fill loops here

        # write output record_data to .tmp files
        output_file_path = temp_path + file_list[0] + ".tmp"
        
        file = open(output_file_path, "w+")
        
        file.write("")
        
        for i in record_data:
            file.write(i + ":" + record_data[i] + "\n")
    
        file.close()


if __name__ == "__main__":
    main(sys.argv)
