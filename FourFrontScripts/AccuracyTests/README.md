# Accuracy Testing

Accuracy testing is performed on sections filled by a data entry personnel. The data entered by the data entry personnel are assumed to be accurate. The Autofill Software is run on these sections and the output is compared with the actual filled MS Access Database. 


### Algorithm
To test the accuracy of the extracted test, we look at three possibilities:
1. **Filled**: The Autofill **and** the MS Access database had the field filled for the given record
2. **Missing**: The Autofill **missed** (empty) the field, while the MS Access database had something filled for that field.
3. **Incorrect**: The Autofill filled it in a field that is empty is the MS Access database so it is definitely **incorrect**.

##### Accuracy
The accuracy was tested on the fields that fell under the **Filled category** using the [**Levenshtein Distance**](https://en.wikipedia.org/wiki/Levenshtein_distance). 
The accuracy is given by:
```
difference = levenshteinDistance(autofill_Field, msAccess_Field)
accuracy  = (len(msAccess_Field) - difference) / len(msAccess_Field)
```

### Run
1. Select a pre-filled section
2. Run the autofill software on this section
3. Add the section in the ```main.py``` in the accuracy tests 
4. Run the ```main.py``` to generate the accuracy results
4. The result for the section is in the [AccuracyResults](https://github.com/FourFront-Senior-Design/Autofill-pythonenv/tree/accuracyTests/FourFrontScripts/AccuracyTests/AccuracyResults) folder
