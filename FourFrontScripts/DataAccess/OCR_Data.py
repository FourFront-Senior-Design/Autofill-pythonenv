import sys, json

class Word:
    text = ""
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    def __init__(self, string, X1, Y1, X2, Y2):
        self.text = string
        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2
        
    def __str__(self):
        return self.text + "\n\tx1: " + str(self.x1) + "\n\ty1: " + str(self.y1) + "\n\tx2: " + str(self.x2) + "\n\ty2: " + str(self.y2)
        
    def getText(self):
        return self.text
        
    def getBoundingBox(self):
        return self.x1, self.y1, self.x2, self.y2

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
                # Get the first file data
                data = json.load(file)
                self.jsonData.append(data)
        except:
            print("Error loading first json file: ", sys.exc_info()[0])
            raise
        
        if (filePath2 is not None):
            try:
                with open(filePath2, 'r') as file:
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
                        textAnnotations[i].get('boundingPoly').get('vertices')[2].get('x'),
                        textAnnotations[i].get('boundingPoly').get('vertices')[2].get('y'))
                        
                    if (side is 0):
                        self.frontWords.append(newWord)
                    else:
                        self.backWords.append(newWord)
            
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
        return self.frontWords, self.backWords
    
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
