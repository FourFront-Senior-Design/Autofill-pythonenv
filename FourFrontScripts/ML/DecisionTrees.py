import sys
import os.path
import string

from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
#from IPython.display import Image
#import pydotplus

import pandas as pd
import numpy as np

def get_data(dataset):
    if os.path.isfile(dataset):
        print("Loading ", dataset, " dataset ...")
        data = pd.read_csv(dataset, engine='python')
        print("\nDataset loaded successfully\n\n")
        return data
    else:
        print('File not found')
        print('\n\nExiting...')
        sys.exit()

dataset = get_data('C:/Python/FourFrontScripts/DataPrep/data.csv')

marker = preprocessing.LabelEncoder()
dataset['markerType'] = marker.fit_transform(dataset['markerType'])
print(marker)
loc = preprocessing.LabelEncoder()
dataset['ImageLocation'] = loc.fit_transform(dataset['ImageLocation'])
category = preprocessing.LabelEncoder()
dataset['category'] = category.fit_transform(dataset['category'])

x = dataset[["markerType", "ImageLocation", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"]]
y = dataset['category']

print(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=2)

dt = DecisionTreeClassifier(max_depth = 10, random_state = 1)
dt.fit(x_train, y_train)

pred = dt.predict(x_test)
print(accuracy_score(y_test, pred))