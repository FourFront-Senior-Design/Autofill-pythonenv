from DataAccess.OCR_Data import OCR_Data
from DataAccess.OCR_Data import Word
from DataStructures.ranks import ranks

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
    
    # Naive approach: Search the ranks map for every word in the string less than the max rank size (6)

    # Get all words from data object
    frontWordList, backWordList = data.getWords()
    
    rankList = list()
    
    # For each word
    for w in frontWordList + backWordList:

        # If the word is less than the max length of a rank (6)
        # and it matches a rank from the rank list
        if w.text in ranks and len(w.text) < 6:
            # Insert into list
            rankList.append(w.text)
            
    # Add ranks to rankMap
    rankMap["Rank"] = None if len(rankList) < 1 else rankList[0]
    rankMap["Rank2"] = None if len(rankList) < 2 else rankList[1]
    rankMap["Rank3"] = None if len(rankList) < 3 else rankList[2]
    rankMap["RankS_D"] = None if len(rankList) < 4 else rankList[3]
    rankMap["Rank2S_D"] = None if len(rankList) < 5 else rankList[4]
    rankMap["Rank3S_D"] = None if len(rankList) < 6 else rankList[5]
    rankMap["RankS_D_2"] = None if len(rankList) < 7 else rankList[6]
    rankMap["RankS_D_3"] = None if len(rankList) < 8 else rankList[7]
    rankMap["RankS_D_4"] = None if len(rankList) < 9 else rankList[8]
        
        
    # return all ranks found
    return rankMap