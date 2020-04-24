# OCR_Data reads the json files in the GoogleVision folder of a given section
import sys, json, os

'''
The word object is used in the OCR_Data object to track individual words and their 
locations in the image. Words are created when an OCR_Data object is created, 
and contain information about the words on the stone.

text: A string containing the contents of the word

There are a few functions that can be used to get information from a word:

getText(): returns text.

getBoundingBox(): returns a tuple of x1, y1, x2, y2, x3, y3, x4, y4.
'''
class Word:
    text = ""
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    x4 = 0
    y4 = 0
    
    def __init__(self, string, X1, Y1, X2, Y2, X3, Y3, X4, Y4):
        self.text = string
        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2
        self.x3 = X3
        self.y3 = Y3
        self.x4 = X4
        self.y4 = Y4
        
    def __str__(self):
        return self.text + "\n\tx1: " + str(self.x1) + "\n\ty1: " + str(self.y1) + "\n\tx2: " + str(self.x2) + "\n\ty2: " + str(self.y2)
        
    def getText(self):
        return self.text
        
    def getBoundingBox(self):
        return [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4]

    
'''
The OCR_Data object is a class which sits between the developers and the json files returned 
from Google Vision. Its constructor takes either one or two paths to json files from Google Vision
and reads data from those to fill out various data structures:

jsonData: a list of either one or two elements, each the full json data from a side 
of the stone. If the stone is an upright you should see two elements in this list.

frontWords: a list of all words (see word object for more documentation) from the front of the stone.

backWords: a list of words from the back of the stone.

fullText: a list of either one or two strings, each the string of text extracted from each 
side of the stone. If the stone is an upright you should see two elements in this list.


OCR_Data provides a few functions to help interact with this data:
getWord(word): This function takes a string and searches the words lists to find it. 
It returns a word (see word object for more documentation).

getWords(): This returns a tuple of frontWords, backWords.

getFullText(): This returns fullText.

getJsonData(): This returns jsonData.

'''
class OCR_Data: 
    jsonData = list()
    frontWords = list()
    backWords = list()
    fullText = list()
    
    '''
    Loads the json data into the OCR_Data object
    '''
    def __init__(self, filePath1 = None, filePath2 = None):
        # Clear all pre-existing data
        self.jsonData.clear()
        self.frontWords.clear()
        self.backWords.clear()
        self.fullText.clear()
    
        # If the first filepath doesn't exist that's an issue
        if (filePath1 is None):
            print("OCR_Data needs at least one filepath! It'll be empty!")
            return
        
        try:
            with open(filePath1, 'r') as file:
                if os.stat(filePath1).st_size > 0:
                    # Get the first file data
                    data = json.load(file)
                    self.jsonData.append(data)
        except:
            print("Error loading first json file: ", sys.exc_info()[0])
            raise
        
        if (filePath2 is not None):
            try:
                with open(filePath2, 'r') as file:
                    if os.stat(filePath2).st_size > 0:
                        # Append the second json file data
                        data = json.load(file)
                        self.jsonData.append(data)
            except:
                print("Error loading second json file: ", sys.exc_info()[0])
                raise
                
        side = 0
        for j in self.jsonData:
            textAnnotations = j.get('textAnnotations')
            if (textAnnotations is not None):
                # Get full text
                text = textAnnotations[0].get('description')
                self.fullText.append(text)
                        
                # Get all the words
                for i in range(1, len(textAnnotations)):
                    newWord = Word(textAnnotations[i].get('description'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[0].get('x'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[0].get('y'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[1].get('x'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[1].get('y'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[2].get('x'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[2].get('y'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[3].get('x'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[3].get('y'))
                        
                    if (side is 0):
                        self.frontWords.append(newWord)
                    else:
                        self.backWords.append(newWord)
            else:
                self.fullText.append("")
            
            side = 1
            
    '''
    Gets a list of matching words in this order: front of stone top to bottom,
    back of stone top to bottom
    '''
    def getWord(self, word):
        word = word.upper()
        wordList = list()
        
        for known in self.frontWords:
            if known.text == word:
                wordList.append(known)
        for known in self.backWords:
            if known.text == word:
                wordList.append(known)
                
        return wordList
    
    '''
    Returns list(s) of words from the front and back of the stone.
    If there is no back image the list will be either null or empty
    '''
    def getWords(self):
        return (self.frontWords, self.backWords)
    
    '''
    Returns a list of full text annotations (all the contents)
    '''
    def getFullText(self):
        return self.fullText
        
    '''
    Returns the source Json data
    '''
    def getJsonData(self):
        return self.jsonData

    def getImageLoc(self, w, coordinate):
        (f, b) = self.getWords()
        word = Word(w, coordinate[0], coordinate[1], coordinate[2],
                    coordinate[3], coordinate[4], coordinate[5], coordinate[6], coordinate[7])

        if word in f:
            return "front"

        return "back"
