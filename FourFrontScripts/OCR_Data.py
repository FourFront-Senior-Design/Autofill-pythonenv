import sys, json
from word import Word

class OCR_Data: 
    jsonData = list()
    frontWords = list()
    backWords = list()
    fullText = list()
    
    def __init__(self, filePath1 = None, filePath2 = None):  
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
        
    def getWords(self):
        return self.frontWords, self.backWords
    
    def getFullText(self):
        return self.fullText
        
    def getJsonData(self):
        return self.jsonData
