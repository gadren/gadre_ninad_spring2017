
# coding: utf-8

# # Q3
# Calculate the average score for each team which host the game and win the game

# In[134]:

import pandas as pd
from pandas import DataFrame
import sys, os, datetime


# In[135]:

path = os.getcwd()+'\\data\\cricket_matches.csv'
path


# In[136]:

df = pd.read_csv(path) #Read data from CSV


# In[137]:

df.head()


# In[138]:

df1 = df[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]
df2 = df1[df1['home'] == df['winner']]
df2.head()


# In[139]:

df2['in1'] = df2['winner'] == df2['innings1']
df2['in2'] = df2['winner'] == df2['innings2']
df2[['home','innings1_runs','innings2_runs','in1','in2']].head()


# In[140]:

df2['TotalScore'] = df2['innings1_runs']*df2['in1'] + df2['innings2_runs']*df2['in2']
df3 = df2[['home','TotalScore']]
df3 = df3.groupby('home').mean().sort_values(by='TotalScore',ascending=False)
df3.head()


# In[142]:

#write to csv
df3.to_csv('Ques03.csv')


# In[ ]:



