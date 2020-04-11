from DataAccess.OCR_Data import OCR_Data
from DataAccess.OCR_Data import Word
from DataStructures.wars import wars

import re

'''
Creates a map of war field to war values that matches the database and fills that map with
wars found in the given data object.
'''
def extractWars(data):
    warMap = {
    'War': '',
    'War2': '',
    'War3': '',
    'War4': '',
    'WarS_D': '',
    'War2S_D': '',
    'War3S_D': '',
    'War4S_D': '',
    'WarS_D_2': '',
    'WarS_D_3': '',
    'WarS_D_4': ''
    }
    
    # Naive approach: Search the string for every war

    # Get all words from data object
    fullText = data.getFullText()
    
    warList = list()
    
    # For each word
    for w in wars:
        # If the key matches a with the string
        if re.match(w, fullText):
            # Insert into list
            warList.append(wars[w])
            
    # Add wars to warMap
    warMap["War"] = "" if len(warList) < 1 else warList[0]
    warMap["War2"] = "" if len(warList) < 2 else warList[1]
    warMap["War3"] = "" if len(warList) < 3 else warList[2]
    warMap["War4"] = "" if len(warList) < 4 else warList[3]
    warMap["WarS_D"] = "" if len(warList) < 5 else warList[4]
    warMap["War2S_D"] = "" if len(warList) < 6 else warList[5]
    warMap["War3S_D"] = "" if len(warList) < 7 else warList[6]
    warMap["War4S_D"] = "" if len(warList) < 8 else warList[7]
    warMap["WarS_D_2"] = "" if len(warList) < 9 else warList[8]
    warMap["WarS_D_3"] = "" if len(warList) < 10 else warList[9]
    warMap["WarS_D_4"] = "" if len(warList) < 11 else warList[10]
        
    # return all wars found
    return warMap
