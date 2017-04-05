
# coding: utf-8

# # Q2_PART ONE
# Find out the highest paid departments in each organization group by
# calculating mean of total compensation for every department

# In[1]:

import pandas as pd
from pandas import DataFrame
import sys, os, datetime


# In[3]:

path = os.getcwd()+'\\data\\employee_compensation.csv'
path


# In[4]:

df = pd.read_csv(path) #Read data from CSV


# In[5]:

df.head()


# In[7]:

df2 = df[['Organization Group','Department','Total Compensation']]
df2.head()


# In[9]:

org = df2['Organization Group'].unique()
org


# In[10]:

dept = df2['Department'].unique()
dept


# In[11]:

orglist = []
for each in org:
    df3 = df2[df2['Organization Group'] == each]
    depts = df3['Department'].unique()
    for every in depts:
        average = df3[df3['Department'] == every].mean()
        orglist.append((each,every,average[0]))
        
avg_comp = DataFrame(orglist,columns=('Organization Group',
                                      'Department',
                                      'Average Compensation')).sort_values(by=['Organization Group',
                                                                               'Department',
                                                                               'Average Compensation'],ascending = False).reset_index(drop=True)
avg_comp.head()


# In[12]:

#write to csv
avg_comp.to_csv('Ques02_Part01.csv',index=False,header=True)


# In[ ]:



