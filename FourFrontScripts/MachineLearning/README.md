# Machine learning

After the [Data Preparation](https://github.com/FourFront-Senior-Design/Autofill-pythonenv/tree/master/FourFrontScripts/DataPreparation) step, we tried to classify the text using the [Random Forest Classifier](https://www.datacamp.com/community/tutorials/random-forests-classifier-python). 

Currently, the ```RandomForestAll.py``` successfully predicts the class, i.e. the column in the database successfully. The function call to predict is:

```
# Gets the markerType, imageLoc(front/back) and coordinates
# of the word to predict the column in which the word would belong

ml = RandomForestAll.RandomForestAll()
column = ml.Predict(markerType, imageLoc, coordinates)
```
