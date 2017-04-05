
# coding: utf-8

# # Q1_PART ONE
# For each month in 2016, find out the percentage of collisions in
# Manhattan out of that year's total accidents in New York City

# In[30]:

import pandas as pd
from pandas import DataFrame
import sys, os, datetime


# In[31]:

path = os.getcwd()+'\\data\\vehicle_collisions.csv'
path


# In[32]:

df = pd.read_csv(path) #Read data from CSV


# In[33]:

#Convert date column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])


# In[34]:

#Filtering data with entries only from 2016
sxtn = df[(df['DATE'] >= '2016-01-01') & (df['DATE'] <= '2016-12-31')]


# In[35]:

sxtn['MONTH'] = sxtn['DATE'].apply(lambda x : x.strftime('%b'))


# In[36]:

month = sxtn['MONTH'].unique()


# In[37]:

df1 = {'MONTH':[],'MANHATTAN':[],'NYC':[],'PERCENTAGE':[]}
for m in month:
    everymonth = sxtn[sxtn['MONTH'] == m]
    nyc = len(everymonth)
    manhat = len(everymonth[everymonth['BOROUGH'] == 'MANHATTAN'])
    percent = manhat/nyc
    
    #store data
    df1['MONTH'].append(m)
    df1['MANHATTAN'].append(manhat)
    df1['NYC'].append(nyc)
    df1['PERCENTAGE'].append(percent)
    
df3 = DataFrame(df1, columns=['MONTH','MANHATTAN','NYC','PERCENTAGE'])
df3.head()


# In[38]:

#write to csv
df3.to_csv('Ques01_Part01.csv',index=False,header=True)


# In[ ]:



