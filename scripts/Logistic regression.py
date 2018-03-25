
# coding: utf-8

# In[1]:


# imports
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from os import (environ, path)
import sys
import calendar
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression


# In[2]:


df = pd.read_csv(path.join(environ['DATA_FOLDER'], "train_sample.csv.zip"))
df.set_index('ip', inplace=True)
print(df.head(5))
print(df.dtypes)


# In[3]:


# Exploding date to dummy values
def explode_date_attributes(dataframe, column_name):

    days = pd.to_datetime(dataframe[column_name]).dt.weekday_name
    dummies_day = pd.get_dummies(days)
    
    hours = pd.to_datetime(dataframe[column_name]).dt.hour
    dummies_hour = pd.get_dummies(hours, prefix='hour')
    
    return pd.concat([dataframe, dummies_day, dummies_hour], axis=1)


df_date_dummy = explode_date_attributes(df, 'click_time')
df_date_dummy = df_date_dummy.drop('click_time', axis='columns')
print(df_date_dummy.head(5))


# In[4]:


# not sure how to use attributed_time yet, just dropping it for now
df_train = df_date_dummy.drop('attributed_time', axis='columns')
print(df_train.head(5))


# In[5]:


# All rest to dummy values
to_dummies = ['app', 'device', 'os', 'channel']
dummies = [pd.get_dummies(df_train[x], prefix=x) for x in to_dummies]
dummies.append(df_train)
df_train = pd.concat(dummies, axis='columns')
df_train.drop(to_dummies, axis='columns')
print(df_train.head(5))


# In[6]:


# Getting features X and dependent variable Y
y = 'is_attributed'
X = [x for x in df_train.columns.values.tolist() if x not in [y]]
print(X)


# In[7]:


# Splitting between train and test in our sample
msk = np.random.rand(len(df)) < 0.8
train = df_train[msk]
test = df_train[~msk]
print(len(train))
print(len(test))


# In[ ]:


# model
print("Training..")
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# n_jobs: -1 to run on all cores
# verbose: 1 (default is 0)
logreg = LogisticRegression(n_jobs=-1, verbose=1)

rfe = RFE(logreg, 18)
rfe = rfe.fit(train[X], train[y])


