import os
import sys
#from os import listdir, mkdir
#from os.path import isfile, join
import json
from copy import deepcopy
import googleVisionOCR
from DataStructures import dataTemplate
from DataAccess.OCR_Data import OCR_Data

# Add extraction module imports here
from Extraction import dateExtraction
from Extraction import rankExtraction


def extract(OCR):
    """Runs extraction scripts and returns data in a single dictionary"""
    # args is: 'full_path\\filename1.json full_path\\filename2.json'
    # filename2 is only present for uprights

    # access empty data template
    # deepcopy here since we do not want to modify the single empty_data dictionary
    record_data = deepcopy(dataTemplate.data_template)

    # Do not call any extraction scripts if OCR is empty
    if OCR:
        ### BEGIN EXTRACTION CALLS ###
        # NOTE: Extraction scripts should only return key/value pairs for extracted data
        # NOTE: Dictionaries from extraction scripts should NOT have any blank or
        #       missing values in key/value pairs (i.e. there should be no key overlap
        #       between the various extractions scripts)
        # NOTE: Add additional extraction script calls here
        # FORMAT: record_data.update(<script_file_name.script_function_name>(OCR))
        record_data.update(dateExtraction.extract_dates(OCR))
        record_data.update(rankExtraction.extractRanks(OCR))

        ### END EXTRACTION CALLS ###
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

        file_1_path = json_path + file_list[0] + ".json"
        file_2_path = None
        if len(file_list) > 1:
            file_2_path = json_path + file_list[1] + ".json"
        
        # Create OCR object
        OCR = OCR_Data(file_1_path, file_2_path)

        # extract data / run extraction scripts
        record_data = extract(OCR)

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
