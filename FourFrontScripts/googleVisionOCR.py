import io
import os

from os import listdir, mkdir
from os.path import isfile, isdir, join, exists
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson

def OCR(filePath):
    # Find the credentials file
    credentialPath = "C:\\Python\\FourFrontScripts\\credentials\\"
    credentialList = [f for f in listdir(credentialPath) if isfile(join(credentialPath, f))]
    
    if len(credentialList) > 1:
        print("TOO MANY CREDENTIALS!!!")
        return
    
    nameParts = credentialList[0].split('.')
    
    print(nameParts)
    if nameParts[1] != "json":
        print("CREDENTIALS NOT CORRECT!!!")
    
    keyPath = credentialPath + credentialList[0]
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=keyPath
    
    client = vision.ImageAnnotatorClient()

    imagePath = filePath + "\\ReferencedImages\\"
    outputPath = filePath + "\\GoogleVisionData\\"
    
    if not os.path.isdir(outputPath):
        os.mkdir(outputPath)
    
    fileList = [f for f in listdir(imagePath) if isfile(join(imagePath, f))]
    for f in fileList:
        nameParts = f.split('.')
        outFilePath = outputPath + nameParts[0] + ".json"

        if nameParts[1] == "jpg":
            if not exists(outFilePath):
                currentImagePath = imagePath + "\\" + f

                with io.open(currentImagePath, 'rb') as image_file:
                    content = image_file.read()

                image = types.Image(content=content)

                response = client.text_detection(image=image)

                outFile = open(outFilePath, 'w+')

                outFile.write(MessageToJson(response))
