
# coding: utf-8

# # Q2_PART TWO
# Display the top 5 Job Families according to this percentage value

# In[2]:

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


# In[6]:

df = df[df['Year Type'] == 'Calendar']
col = ['Year'] + list(df.loc[:,'Salaries':'Total Compensation'])
sal = df[col]


# In[7]:

temp = []
for each in df['Year'].unique():
    year = sal[sal['Year'] == each]
    value = year.mean()
    temp.append((each,value['Salaries'],
               value['Overtime'],
               value['Other Salaries'],
               value['Total Salary'],
               value['Retirement'],
               value['Health/Dental'],
               value['Other Benefits'],
               value['Total Benefits'],
               value['Total Compensation']))
    
avg_comp = DataFrame(temp,columns=('Year',
                                   'Salaries',
                                  'Overtime',
                                  'Other Salaries',
                                   'Total Salary',
                                  'Retirement',
                                  'Health/Dental',
                                  'Other Benefits',
                                  'Total Benefits',
                                  'Total Compensation')).sort_values(by='Year').reset_index(drop=True)

avg_comp.head()


# In[8]:

#overtime greater than 5%
df[df['Overtime'] > (df['Salaries']*0.05)].head()


# In[9]:

temp = []
for every in df['Job Family'].unique():
    benefits = df[df['Job Family'] == every]['Total Benefits'].mean()
    comp = df[df['Job Family'] == every]['Total Compensation'].mean()
    percent = (benefits/comp)*100
    temp.append((every,benefits,comp,percent))
    
percent_comp = DataFrame(temp,columns=('Job Family',
                                      'Total Benefits',
                                      'Total Compensation',
                                      'Percentage')).sort_values(by='Percentage',ascending=False).reset_index(drop=True)
percent_comp.head()


# In[10]:

#write to csv
percent_comp.to_csv('Ques02_Part02.csv',index=False,header=True)


# In[ ]:



