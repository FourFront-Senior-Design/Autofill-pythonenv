from DataAccess.OCR_Data import OCR_Data
from DataAccess.OCR_Data import Word
from DataStructures.ranks import ranks

import re

'''
Creates a map of Rank field to rank values that matches the database and fills that map with
ranks found in the given data object.
'''
def extractRanks(data):
    rankMap = {
    'Rank': '',
    'Rank2': '',
    'Rank3': '',
    'RankS_D': '',
    'Rank2S_D': '',
    'Rank3S_D': '',
    'RankS_D_2': '',
    'RankS_D_3': '',
    'RankS_D_4': ''
    }
    
    # Get all words from data object
    sides = data.getFullText()
    
    frontRankList = list()
    backRankList = list()
    side = 0

    for s in sides:
        # For each key in wars
        for r in ranks:
            # If there is a space in the rank, replace the space with a \s for regex
            if " " in r:
                parts = r.split()
                searchString = "[\s\n,.]" + parts[0] + "\s" + parts[1] + "[\s\n,.]"
            else:
                searchString = "[\s\n,.]" + r + "[\s\n,.]"

            # If the key matches with the string
            matches = re.finditer(searchString, s)

            if matches is not None:
                for m in matches:
                    print(searchString, r)
                    # Insert into list
                    if side == 0:
                        frontRankList.append(r)
                    else:
                        backRankList.append(r)

                    s = s.replace(r, "")

        side = 1
    
    # Add ranks to rankMap
    rankMap["Rank"] = "" if len(frontRankList) < 1 else frontRankList[0]
    rankMap["Rank2"] = "" if len(frontRankList) < 2 else frontRankList[1]
    rankMap["Rank3"] = "" if len(frontRankList) < 3 else frontRankList[2]
    rankMap["RankS_D"] = "" if len(backRankList) < 1 else backRankList[0]
    rankMap["Rank2S_D"] = "" if len(backRankList) < 2 else backRankList[1]
    rankMap["Rank3S_D"] = "" if len(backRankList) < 3 else backRankList[2]
    rankMap["RankS_D_2"] = "" if len(backRankList) < 4 else backRankList[3]
    rankMap["RankS_D_3"] = "" if len(backRankList) < 5 else backRankList[4]
    rankMap["RankS_D_4"] = "" if len(backRankList) < 6 else backRankList[5]
        
    # return all ranks found
    return rankMap