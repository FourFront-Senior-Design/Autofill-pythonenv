#!/usr/bin/env python
# coding: utf-8

import re
from os import listdir
from os.path import isfile, join, splitext
import copy
from datetime import datetime as dt
import json

import dataTemplate

def month_to_number(month_string):
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
    input_string = input_string.replace('O', '0')
    input_string = input_string.replace('o', '0')
    input_string = input_string.replace('l', '1')
    input_string = input_string.replace('I', '1')
    input_string = input_string.replace('B', '8')
    input_string = input_string.replace('S', '5')
    input_string = input_string.replace('Q', '0')
    return input_string

def updateDateOrder(dates):
    len_dates = len(dates)
    # set len_dates to largest even number
    if len_dates % 2 != 0:
        len_dates -= 1
    for i in range(0, len_dates, 2):
        try:
            firstDate = dt.strptime(dates[i], "%m/%d/%Y")
            secondDate = dt.strptime(dates[i+1], "%m/%d/%Y")
            if secondDate < firstDate:
                # swap dates
                temp = dates[i]
                dates[i] = dates[i+1]
                dates[i+1] = temp
        except:
            pass
    return dates


def parse_args_to_file_list(args):
    # input args is a tuple, and args[0] contains all the input file paths as a string
    # split into a files list, with each item as a string of the input file path
    if (args[0]):
        return args[0].split()


def extractDates(*args):
    out_data = {}

    # regex to select dates
    re_dates = r'(JAN(?:UARY)?|FEB(?:RUARY)?|MAR(?:CH)?|APR(?:IL)?|MAY|JUN(?:E)?|JUL(?:Y)?|AUG(?:UST)?|SEP(?:TEMBER)?|OCT(?:OBER)?|NOV(?:EMBER)?|DEC(?:EMBER)?)\s+([\doOlIBSQ]{1,2})[,.]?\s+([\doOlIBSQ]{4})'

    dates = list()

    # set up date key list (dkl)
    dkl = ['BirthDate', 'DeathDate', 'BirthDateS_D', 'DeathDateS_D',
           'BirthDateS_D_2', 'DeathDateS_D_2', 'BirthDateS_D_3', 'DeathDateS_D_3',
           'BirthDateS_D_4', 'DeathDateS_D_4', 'BirthDateS_D_5', 'DeathDateS_D_5',
           'BirthDateS_D_6', 'DeathDateS_D_6']

    extractedData = list()

    # set up list containing file names
    files = str()
    files = parse_args_to_file_list(args)

    # iterate through input files and append data to extractedData
    # files should contain only one item for flat markers, and two items for uprights
    try:
        for f in files:
            with open(f, 'r') as file:
                    data = json.load(file)
                    extractedData.append(data)
    except:
        pass

    # get text annotations and combine into one string
    extractedText = list()
    combinedText = str()
    for jsonData in extractedData:
        print(jsonData)
        if jsonData.get('textAnnotations') is not None:
            # this specifically grabs only the text annotations in the json data
            text = jsonData.get('textAnnotations')[0].get('description')
            extractedText.append(text)
    # combine text into one string
    if len(extractedText) == 1:
        combinedText = extractedText[0]
    elif len(extractedText) == 2:
        combinedText = extractedText[0] + '\n' + extractedText[1]

    #it_dates is an regex iterator over the combined text string
    it_dates = re.finditer(re_dates, combinedText)
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

    # put dates into out_data
    # if there is only one date, it goes into the DeathDate field, not the BirthDate field
    len_dates = len(dates)
    if len_dates != 0:
        ordered_dates = updateDateOrder(dates)
        if len_dates % 2 == 0:
            for i in range(len_dates):
                out_data[dkl[i]] = ordered_dates[i]
        else:
            for j in range(len_dates - 1):
                out_data[dkl[j]] = ordered_dates[j]
                # this enters the last odd date into the DeathDate field (dkl[len_dates]), not BirthDate field
            out_data[dkl[len_dates]] = ordered_dates[len_dates - 1]

    # this returns a list of key/value pairs for the date fields only
    # it is the controller's responsibility to package these into the larger key/value pairs
    return out_data
