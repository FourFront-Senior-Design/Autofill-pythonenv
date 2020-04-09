import sys
sys.path.append("C:/Python/FourFrontScripts")
import json
import controller
from DataAccess.OCR_Data import OCR_Data
from Extraction.rankExtraction import extractRanks

# Load json data into OCR_Data object
file_path = "C:/Python/FourFrontScripts/tests/resources/test2_front.json"
data = OCR_Data(file_path)

# Get the ranks
rankMap = extractRanks(data)

# Display them
print(rankMap)

# Assert that certain fields match
assert rankMap["Rank"] == "CPL"