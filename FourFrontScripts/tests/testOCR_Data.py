import json, io, sys

sys.path.append("C:/Python/FourFrontScripts")

from OCR_Data import OCR_Data

def main(argv):
    #f1 = "C:\\Python\\FourFrontScripts\\tests\\Resources\\test1.json"
    f1 = "C:\\Python\\FourFrontScripts\\tests\\resources\\test2_front.json"
    f2 = "C:\\Python\\FourFrontScripts\\tests\\resources\\test2_back.json"
    
    object = OCR_Data(f1, f2)
    
    print(object.getFullText())
    print("===========================================")
    
    for side in object.getWords():
        for w in side:
            print(w)
        print("===========================================")
    
    print("===========================================")
    
    foundWords = object.getWord("Ida")
    
    for f in foundWords:
        print(f)

if __name__ == "__main__":
    main(sys.argv)
