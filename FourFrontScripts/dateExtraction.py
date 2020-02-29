#!/usr/bin/env python
# coding: utf-8

import re
from os import listdir
from os.path import isfile, join, splitext
import copy
from datetime import datetime as dt
import json

import dataTemplate


def args_to_file_list(args):
    """Returns list of file names from singleton tuple of file names"""
    # input args is a tuple, and args[0] contains all the input file paths as a string
    # split into a files list, with each item as a string of the input file path
    if args[0]:
        return args[0].split()


def get_json_data(files):
    """Returns list of full json data from list of json file names"""
    # iterate through input files and append data to extracted_data
    extracted_data = list()
    try:
        for f in files:
            with open(f, 'r') as file:
                data = json.load(file)
                extracted_data.append(data)
    except:
        pass
    return extracted_data


def get_text_annotations(extracted_data):
    """Returns list of extracted text annotations from list of full json data"""
    extracted_text = list()
    for jsonData in extracted_data:
        if jsonData.get('textAnnotations') is not None:
            # this specifically grabs only the text annotations in the json data
            text = jsonData.get('textAnnotations')[0].get('description')
            extracted_text.append(text)
    return extracted_text


def merge_text(extracted_text):
    """Returns merged single string from list of two strings"""
    combined_text = str()
    # combine text into one string
    if len(extracted_text) == 1:
        combined_text = extracted_text[0]
    elif len(extracted_text) == 2:
        combined_text = extracted_text[0] + '\n' + extracted_text[1]
    return combined_text


def parse_regex_dates(it_dates):
    """Returns list of dates from regex iterator on dates"""
    dates = list()
    for date in it_dates:
        month = date.groups()[0]
        day = date.groups()[1]
        year = date.groups()[2]
        # convert month to numerical value
        month = month_to_number(month)

        # replace non-digits in day
        day = replace_non_digits(day)

        # add a leading zero for single digits
        if len(day) == 1:
            day = '0' + day

        # replace non-digits in year
        year = replace_non_digits(year)

        # format date
        new_date = str(month + '/' + day + '/' + year)
        dates.append(new_date)
    return dates


def month_to_number(month_string):
    """Converts the name of a month to the month number"""
    m = ''
    if month_string == 'JAN' or month_string == 'JANUARY':
        m = '01'
    elif month_string == 'FEB' or month_string == 'FEBRUARY':
        m = '02'
    elif month_string == 'MAR' or month_string == 'MARCH':
        m = '03'
    elif month_string == 'APR' or month_string == 'APRIL':
        m = '04'
    elif month_string == 'MAY':
        m = '05'
    elif month_string == 'JUN' or month_string == 'JUNE':
        m = '06'
    elif month_string == 'JUL' or month_string == 'JULY':
        m = '07'
    elif month_string == 'AUG' or month_string == 'AUGUST':
        m = '08'
    elif month_string == 'SEP' or month_string == 'SEPTEMBER':
        m = '09'
    elif month_string == 'OCT' or month_string == 'OCTOBER':
        m = '10'
    elif month_string == 'NOV' or month_string == 'NOVEMBER':
        m = '11'
    elif month_string == 'DEC' or month_string == 'DECEMBER':
        m = '12'
    return m


def replace_non_digits(input_string):
    """Replaces non-digits in known dates with digits"""
    input_string = input_string.replace('O', '0')
    input_string = input_string.replace('o', '0')
    input_string = input_string.replace('l', '1')
    input_string = input_string.replace('I', '1')
    input_string = input_string.replace('B', '8')
    input_string = input_string.replace('S', '5')
    input_string = input_string.replace('Q', '0')
    return input_string


def populate_output_dict(dates):
    """Returns dictionary of key/value pairs for dates (database field names/dates)"""
    # set up date key list (dkl) and out_data dictionary
    out_data = {}
    dkl = ['BirthDate', 'DeathDate', 'BirthDateS_D', 'DeathDateS_D',
           'BirthDateS_D_2', 'DeathDateS_D_2', 'BirthDateS_D_3', 'DeathDateS_D_3',
           'BirthDateS_D_4', 'DeathDateS_D_4', 'BirthDateS_D_5', 'DeathDateS_D_5',
           'BirthDateS_D_6', 'DeathDateS_D_6']

    # put dates into out_data
    # if there is only one date, it goes into the DeathDate field, not the BirthDate field
    len_dates = len(dates)
    if len_dates != 0:
        ordered_dates = update_date_order(dates)
        if len_dates % 2 == 0:
            for i in range(len_dates):
                out_data[dkl[i]] = ordered_dates[i]
        else:
            for j in range(len_dates - 1):
                out_data[dkl[j]] = ordered_dates[j]
                # this enters the last odd date into the DeathDate field (dkl[len_dates]), not BirthDate field
            out_data[dkl[len_dates]] = ordered_dates[len_dates - 1]
    return out_data


def update_date_order(dates):
    """Places two date strings in oldest to more recent order"""
    len_dates = len(dates)
    # set len_dates to largest even number
    if len_dates % 2 != 0:
        len_dates -= 1
    for i in range(0, len_dates, 2):
        try:
            first_date = dt.strptime(dates[i], "%m/%d/%Y")
            second_date = dt.strptime(dates[i+1], "%m/%d/%Y")
            if second_date < first_date:
                # swap dates
                temp = dates[i]
                dates[i] = dates[i+1]
                dates[i+1] = temp
        except:
            pass
    return dates


def extract_dates(*args):
    """Returns key/value pairs of dates from .json files (given file names)"""
    # set up list containing file names
    files = args_to_file_list(args)

    # files should contain only one item for flat markers, and two items for uprights
    # extracted_data list contains the full json data in this format ["full_json_for_first", "full_json_for_second"]
    extracted_data = get_json_data(files)

    # get text annotations and combine into one string
    extracted_text = get_text_annotations(extracted_data)

    # merge text into combined text string
    combined_text = merge_text(extracted_text)

    # compile regex to select dates
    # TODO(jd): re-write this long regular expression using
    #           re.verbose, and add comments for each sub-expression
    re_dates = r'(JAN(?:UARY)?|FEB(?:RUARY)?|MAR(?:CH)?|APR(?:IL)?|MAY|JUN(?:E)?|JUL(?:Y)?|AUG(?:UST)?|SEP(?:TEMBER)?|OCT(?:OBER)?|NOV(?:EMBER)?|DEC(?:EMBER)?)\s+([\doOlIBSQ]{1,2})[,.]?\s+([\doOlIBSQ]{4})'
    regex_dates = re.compile(re_dates)

    # it_dates is a regex iterator over the combined text string
    it_dates = re.finditer(regex_dates, combined_text)

    # parse dates from regex iterator
    dates = parse_regex_dates(it_dates)

    # populate output dictionary of key/value pairs (database field name / date)
    out_data = populate_output_dict(dates)

    # this returns a list of key/value pairs for the date fields only
    # it is the controller's responsibility to package these into the full key/value pairs dictionary
    return out_data

