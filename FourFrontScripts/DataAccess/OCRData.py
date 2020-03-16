from DataStructures import dataTemplate
import json

def month_to_number(month_string):
    m = month_string
    if month_string == 'JAN' or month_string == 'JANUARY':
        m = '1'
    elif month_string == 'FEB' or month_string == 'FEBRUARY':
        m = '2'
    elif month_string == 'MAR' or month_string == 'MARCH':
        m = '3'
    elif month_string == 'APR' or month_string == 'APRIL':
        m = '4'
    elif month_string == 'MAY':
        m = '5'
    elif month_string == 'JUN' or month_string == 'JUNE':
        m = '6'
    elif month_string == 'JUL' or month_string == 'JULY':
        m = '7'
    elif month_string == 'AUG' or month_string == 'AUGUST':
        m = '8'
    elif month_string == 'SEP' or month_string == 'SEPTEMBER':
        m = '9'
    elif month_string == 'OCT' or month_string == 'OCTOBER':
        m = '10'
    elif month_string == 'NOV' or month_string == 'NOVEMBER':
        m = '11'
    elif month_string == 'DEC' or month_string == 'DECEMBER':
        m = '12'
    return m

class OCRData:

    def __init__(self, frontPath, backPath):
        self.emptyData = dataTemplate.data_template
        self.jsonDataFront = None
        with open(frontPath, 'r') as file:
            try:
                self.jsonDataFront = json.load(file)
            except:
                pass
        self.jsonDataBack = None
        if backPath != "":
            with open(backPath, 'r') as file:
                try:
                    self.jsonDataBack = json.load(file)
                except:
                    pass
        self.usedFront = []
        self.usedBack = []

    '''
    GetFullText merges the text on the front 
    and back of the headstone
    '''
    def getFullText(self):
        front = self.jsonDataFront['textAnnotations'][0]['description']
        back = ""
        if self.jsonDataBack != None:
            back = self.jsonDataBack['textAnnotations'][0]['description']
        return front + back

    '''
    Gets the words from the ocr data. Makes sure that if it
    is a month, it converts it to a number
    '''
    def getWordList(self):
        textsFront = self.jsonDataFront['textAnnotations']
        textsBack = None
        lenBack = 0
        if self.jsonDataBack != None:
            textsBack = self.jsonDataBack['textAnnotations']
            lenBack = len(textsBack)
        lenFront = len(textsFront)
        wordList = []
        for i in range(1, lenFront):
            wordList.append(month_to_number(textsFront[i]['description']))
        for i in range(1, lenBack):
            wordList.append(month_to_number(textsBack[i]['description']))
        return wordList

    '''
    Gets the coordinates of the word. The usedFront and usedBack is
    used to help navigate the word correctly incase it occurs multiple
    times
    '''
    def getCoordinatesLocation(self, word):
        textsFront = self.jsonDataFront['textAnnotations']
        textsBack = None
        lenBack = 0
        if self.jsonDataBack != None:
            textsBack = self.jsonDataBack['textAnnotations']
            lenBack = len(textsBack)
        lenFront = len(textsFront)
        for i in range(lenFront):
            if month_to_number(textsFront[i]['description']) == word and i not in self.usedFront:
                self.usedFront.append(i)
                return textsFront[i]['boundingPoly']['vertices'], "front"
        for i in range(lenBack):
            if month_to_number(textsBack[i]['description']) == word and i not in self.usedBack:
                self.usedBack.append(i)
                return textsBack[i]['boundingPoly']['vertices'], "back"
        return [], ""

