#!/usr/bin/env python
# coding: utf-8

import json
import re
from os import listdir
from os.path import isfile, join, splitext
import copy


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
    return input_string

def main():
    path = 'C:/Python/FourFrontScripts/tempFiles/'

    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    extension = '.json'
    files = []
    for file in all_files:
        filename, file_extension = splitext(file)
        if file_extension == extension:
            files.append(path + file)

    data_template = {
        'Gravesite #': '',
        'Marker Type': '',
        'Emblem1': '',
        'Emblem2': '',
        'First Name': '',
        'Middle Name': '',
        'Last Name': '',
        'Suffix': '',
        'Location': '',
        'Rank': '',
        'Rank2': '',
        'Rank3': '',
        'Branch': '',
        'Branch2': '',
        'Branch3': '',
        'Branch-Unit_CustomV': '',
        'War': '',
        'War2': '',
        'War3': '',
        'War4': '',
        'BirthDate': '',
        'DeathDate': '',
        'Award': '',
        'Award2': '',
        'Award3': '',
        'Award4': '',
        'Award5': '',
        'Award6': '',
        'Award7': '',
        'Awards_Custom': '',
        'Inscription': '',

        'First Name Spouse/Dependent': '',
        'Middle Name Spouse/Dependent': '',
        'Last Name Spouse/Dependent': '',
        'Suffix Spouse/Dependent': '',
        'LocationS_D': '',
        'RankS_D': '',
        'Rank2S_D': '',
        'Rank3S_D': '',
        'BranchS_D': '',
        'Branch2S_D': '',
        'Branch3S_D': '',
        'Branch-Unit_CustomS_D': '',
        'WarS_D': '',
        'War2S_D': '',
        'War3S_D': '',
        'War4S_D': '',
        'BirthDateS_D': '',
        'DeathDateS_D': '',
        'AwardS_D': '',
        'Award2S_D': '',
        'Award3S_D': '',
        'Award4S_D': '',
        'Award5S_D': '',
        'Award6S_D': '',
        'Award7S_D': '',
        'Awards_CustomS_D': '',
        'InscriptionS_D': '',

        'FirstNameS_D_2': '',
        'MiddleNameS_D_2': '',
        'LastNameS_D_2': '',
        'SuffixS_D_2': '',
        'LocationS_D_2': '',
        'RankS_D_2': '',
        'BranchS_D_2': '',
        'WarS_D_2': '',
        'BirthDateS_D_2': '',
        'DeathDateS_D_2': '',
        'AwardS_D_2': '',
        'InscriptionS_D_2': '',

        'FirstNameS_D_3': '',
        'MiddleNameS_D_3': '',
        'LastNameS_D_3': '',
        'SuffixS_D_3': '',
        'LocationS_D_3': '',
        'RankS_D_3': '',
        'BranchS_D_3': '',
        'WarS_D_3': '',
        'BirthDateS_D_3': '',
        'DeathDateS_D_3': '',
        'AwardS_D_3': '',
        'InscriptionS_D_3': '',

        'FirstNameS_D_4': '',
        'MiddleNameS_D_4': '',
        'LastNameS_D_4': '',
        'SuffixS_D_4': '',
        'LocationS_D_4': '',
        'RankS_D_4': '',
        'BranchS_D_4': '',
        'WarS_D_4': '',
        'BirthDateS_D_4': '',
        'DeathDateS_D_4': '',
        'AwardS_D_4': '',
        'InscriptionS_D_4': '',

        'FirstNameS_D_5': '',
        'MiddleNameS_D_5': '',
        'LastNameS_D_5': '',
        'SuffixS_D_5': '',
        'LocationS_D_5': '',
        'BirthDateS_D_5': '',
        'DeathDateS_D_5': '',

        'FirstNameS_D_6': '',
        'MiddleNameS_D_6': '',
        'LastNameS_D_6': '',
        'SuffixS_D_6': '',
        'LocationS_D_6': '',
        'BirthDateS_D_6': '',
        'DeathDateS_D_6': ''
    }
    # regex to select dates
    re_dates = r'(JAN(?:UARY)?|FEB(?:RUARY)?|MAR(?:CH)?|APR(?:IL)?|MAY|JUN(?:E)?|JUL(?:Y)?|AUG(?:UST)?|SEP(?:TEMBER)?|OCT(?:OBER)?|NOV(?:EMBER)?|DEC(?:EMBER)?)\s+([\doOlI]{1,2})[,.]?\s+([\doOlI]{4})'

    dates = list()

    # set up date key list (dkl)
    dkl = ['BirthDate', 'DeathDate', 'BirthDateS_D', 'DeathDateS_D',
           'BirthDateS_D_2', 'DeathDateS_D_2', 'BirthDateS_D_3', 'DeathDateS_D_3',
           'BirthDateS_D_4', 'DeathDateS_D_4', 'BirthDateS_D_5', 'DeathDateS_D_5',
           'BirthDateS_D_6', 'DeathDateS_D_6']

    # loop to process all files in directory
    for filename in files:
        # print(filename + ':')
        with open(filename, 'r') as file:
            data = json.load(file)
        extracted_text = data.get('textAnnotations')[0].get('description')
        # it_dates is an iterator over the search results
        it_dates = re.finditer(re_dates, extracted_text)
        dates = list()
        for date in it_dates:
            # print(date.groups())
            month = date.groups()[0]
            day = date.groups()[1]
            year = date.groups()[2]
            # convert month to numerical value
            month = month_to_number(month)

            # replace non-digits in day
            day = replace_non_digits(day)

            # replace non-digits in year
            year = replace_non_digits(year)

            # NOTE: We may not need the '/' separator here if we are populating the database
            # with this string, i.e. concatenated date such as 01012000 might work here
            # depending on their database date field settings
            new_date = str(month + '/' + day + '/' + year)
            dates.append(new_date)
        # either load existing data or write to a new data file
        filename = filename.split('/')[4]
        print(filename)
        datafile = 'C:/Python/FourFrontScripts/results/' + filename.strip('.json') + '.data'
        try:
            with open(datafile) as f:
                # Read data file into out_data
                out_data = json.load(f)
        except FileNotFoundError:
            # Create out_data from blank data_template
            out_data = copy.deepcopy(data_template)

        # put dates into out_data
        # if there is only one date, it goes into the DeathDate field, not the BirthDate field
        len_dates = len(dates)
        if len_dates == 0:
            pass
        elif len_dates % 2 == 0:
            for i in range(len_dates):
                out_data[dkl[i]] = dates[i]
        else:
            for j in range(len_dates - 1):
                out_data[dkl[j]] = dates[j]
                # this enters the last odd date into the DeathDate field (dkl[len_dates]), not BirthDate field
            out_data[dkl[len_dates]] = dates[len_dates - 1]
        # write out_data to file
        print(datafile)
        with open(datafile, 'w', encoding="utf-8", newline='\r\n') as f:
            out_data = json.dump(out_data, f, indent=4, sort_keys=True, ensure_ascii=False)

            # display the dates (debugging)
        # for i in dates:
        #    print(i, end=' ')
        # print('\n')

if __name__ == "__main__":
    main()
