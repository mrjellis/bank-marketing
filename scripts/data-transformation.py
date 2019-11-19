import pandas as pd
import numpy as np
import os

np.set_printoptions(threshold=2000)
os.getcwd()


os.chdir('.\scripts')

#imports the datasource retrieved from the custom Postgressql Database. 
#alternatively, pd.read_csv('bank-full.csv') would work also

import connect #the python script to retrieve data from database

df = connect.df
df.head(10)
data = df

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

#columns to create labels for

cols = ['job','marital','education','default','housing','loan','month']

#Label encodes all of the columns in cols; adds new columns with encoded values. 
for i in cols:
    data[i+'_cats'] = labelencoder.fit_transform(data[i])
    
df.drop(['contact','id'])

def binary_function(self):
    if self =='yes':
        return 1
    else:
        return 0

df['y'] = df['y'].apply(binary_function)


df.drop(['id'])

data1 = data.drop(cols,axis=1)

#export data to csv called "Transformed Data.csv"
data1.to_csv('../Data/Transformed Data.csv',index=False)

