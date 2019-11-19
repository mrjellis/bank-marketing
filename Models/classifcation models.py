import pandas as pd
import numpy as np

import os

#imports from the Transformed Data.csv
df = pd.read_csv('../Data/Transformed Data.csv')
df = df.drop(['id','contact','poutcome'],axis=1)

#creats one hot encoder for the target variable
def binary_function(self):
    if self =='yes':
        return 1
    else:
        return 0


X = df.drop('y',axis=1)
y = df['y'].apply(binary_function)

#train test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split( X, 
    y, test_size=0.33, random_state=42)

#logistic regression
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)

#tests for accuracy
from sklearn.metrics import roc_curve,confusion_matrix,auc,accuracy_score,classification_report

confusion_matrix(y_test,y_pred)
accuracy_score(y_test,y_pred)
print(classification_report(y_test,y_pred))


#Random Forrest Regression Tree

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier()

forest.fit(X_train,y_train)

feature_import = forest.feature_importances_
feats = pd.DataFrame(feature_import,columns=['Importance'])
names = pd.DataFrame(X_train.columns,columns=['Feat Name'])
feature_importances = pd.concat([feats,names],axis=1)
feature_importances.sort_values(by=['Importance'],ascending=False)

Y_forest_pred = forest.predict(X_test)

print(classification_report(y_test,Y_forest_pred))

accuracy_score(y_test,Y_forest_pred)


#knearest neighbors
##
from sklearn.neighbors import KNeighborsClassifier

knn  = KNeighborsClassifier()

knn.fit(X_train,y_train)

#choosing optimal K neighbors using the elbow method

error_rate = []

for i in range(1,40):

    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

import matplotlib.pyplot as plt


plt.figure(figsize=(12,10))

plt.plot(range(1,40),error_rate,color='blue',marker='o',markerfacecolor='red')


knn = KNeighborsClassifier(n_neighbors=25)

knn.fit(X_train,y_train)

knn_pred = knn.predict(X_test)

print(classification_report(y_test,knn_pred))

accuracy_score(y_test,knn_pred)