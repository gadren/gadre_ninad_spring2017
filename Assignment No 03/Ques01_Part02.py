
# coding: utf-8

# # Q1_PART TWO
# For each borough, find out distribution of each collision scale. (One car
# involved? Two? Three? or more?) (From 2015 to present)

# In[8]:

import pandas as pd
from pandas import DataFrame
import sys, os, datetime


# In[15]:

path = os.getcwd()+'\\data\\vehicle_collisions.csv'
path


# In[16]:

df = pd.read_csv(path) #Read data from CSV


# In[17]:

df['BOROUGH'].fillna('UNRECORDED',inplace=True)
borough = df['BOROUGH'].unique()


# In[22]:

collision = []
for b in borough:
    bor = df[df['BOROUGH'] == b]
    vehicle = bor.loc[:,'VEHICLE 1 TYPE': 'VEHICLE 5 TYPE']
    vehicle['NUM'] = vehicle.count(axis=1)
    
    value = vehicle['NUM'].value_counts()
    
    collision.append((b,value[1],value[2],value[3],(value[4]+value[5])))
    
vehcol = DataFrame(collision, columns=('BOROUGH','1-VEHICLE','2-VEHICLE','3-VEHICLE','More Than 3 VEHICLES')).sort_values(by='BOROUGH')

vehcol.head()


# In[23]:

vehcol.to_csv('Ques01_Part02.csv',index=False,header=True)


# In[ ]:



