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
    sides = data.getFullText()
    
    frontWarList = list()
    backWarList = list()
    side = 0

    for s in sides:
        # For each key in wars
        for w in wars:
            searchString = "[\s\n,.]" + w + "[\s\n,.]"
        
            # If the key matches with the string
            matches = re.search(searchString, s)
            if matches is not None:
                # Insert into list
                if side == 0:
                    frontWarList.append(wars[w])
                else:
                    backWarList.append(wars[w])
        
        side = 1

    
                
    # Add wars to warMap
    warMap["War"] = "" if len(frontWarList) < 1 else frontWarList[0]
    warMap["War2"] = "" if len(frontWarList) < 2 else frontWarList[1]
    warMap["War3"] = "" if len(frontWarList) < 3 else frontWarList[2]
    warMap["War4"] = "" if len(frontWarList) < 4 else frontWarList[3]
    warMap["WarS_D"] = "" if len(backWarList) < 1 else backWarList[0]
    warMap["War2S_D"] = "" if len(backWarList) < 2 else backWarList[1]
    warMap["War3S_D"] = "" if len(backWarList) < 3 else backWarList[2]
    warMap["War4S_D"] = "" if len(backWarList) < 4 else backWarList[3]
    warMap["WarS_D_2"] = "" if len(backWarList) < 5 else backWarList[4]
    warMap["WarS_D_3"] = "" if len(backWarList) < 6 else backWarList[5]
    warMap["WarS_D_4"] = "" if len(backWarList) < 7 else backWarList[6]
        
    # return all wars found
    return warMap
