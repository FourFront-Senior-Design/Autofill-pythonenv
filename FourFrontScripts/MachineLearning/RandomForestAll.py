# random forest classifier to predict categories (columns)

from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

class RandomForestAll:
    _dataset = r'C:/Python/FourFrontScripts/TestData/data.csv'

    # Reads the data
    def __init__(self):
        self._dataframe = pd.read_csv(self._dataset, engine='python')

    # Converts the columms into categorical variables
    def __preprocessing(self):
        self.__marker = preprocessing.LabelEncoder()
        self.__loc = preprocessing.LabelEncoder()
        self.__category = preprocessing.LabelEncoder()
        self._dataframe['markerType'] = self.__marker.fit_transform(self._dataframe['markerType'])
        self._dataframe['ImageLocation'] = self.__loc.fit_transform(self._dataframe['ImageLocation'])
        self._dataframe['category'] = self.__category.fit_transform(self._dataframe['category'])

    # Splits the data into training and testing datasets
    def __trainTestSplit(self):
        x = self._dataframe[["markerType", "ImageLocation", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"]]
        y = self._dataframe['category']
        self.__x_train,self.__x_test,self.__y_train,self.__y_test=train_test_split(x,y,test_size=0.1, random_state=2)

    # Makes the decision tree
    def __makeModel(self):
        self.__dt = RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0)
        self.__dt.fit(self.__x_train, self.__y_train)

    # Internal Use Only: Used to get the accuracy of the model
    def __getAccuracy(self):
        pred = self.__dt.predict(self.__x_test)
        acc = accuracy_score(self.__y_test, pred)
        #print("Accuracy of DecisionTreeAll: ", str(acc))

    # Gets the markerType, imageLoc(front/back) and coordinates
    # to predict the column in which the word would belong
    def Predict(self, markerType, imageLoc, coordinates):
        self.__preprocessing()
        self.__trainTestSplit()
        self.__makeModel()

        x1, y1 = coordinates[0]['x'], coordinates[0]['y']
        x2, y2 = coordinates[1]['x'], coordinates[1]['y']
        x3, y3 = coordinates[2]['x'], coordinates[2]['y']
        x4, y4 = coordinates[3]['x'], coordinates[3]['y']
        markerType = self.__marker.fit_transform([markerType])
        imageLoc = self.__loc.fit_transform([imageLoc])

        data = [markerType, imageLoc, x1, y1, x2, y2, x3, y3, x4, y4]
        data = np.asarray(data)
        data = data.reshape(1, -1)
        predCategoryNum = self.__dt.predict(data)
        predCategory = self.__category.inverse_transform(predCategoryNum)[0]
        return predCategory
