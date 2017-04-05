
# coding: utf-8

# # Q4_PART ONE
# You are supposed to extract data from the awards column in this dataset and split it into several
# columns

# In[47]:

import pandas as pd
from pandas import DataFrame
import sys, os, datetime


# In[48]:

path = os.getcwd()+'\\data\\movies_awards.csv'
path


# In[49]:

df = pd.read_csv(path) #Read data from CSV


# In[50]:

df.head()


# In[51]:

df = df[df['Awards'].notnull()]
df['Awards_won'] = df['Awards'].str.extract('(\d+) win', expand=True)
df['Awards_nominated'] = df['Awards'].str.extract('(\d+) nomination', expand=True)


# In[52]:

#function to take plurals into count
def strip_plural(title):
    if str(title).endswith('s'):
        return str(title)[:-1]
    else:
        return str(title)


# In[53]:

#extract name and count of award
df[['AwardCount','AwardWon']] = df['Awards'].str.extract('Won (\d+) (.*). Another', expand=True)
#extract name and count of nomination
df[['NominatedCount','AwardNominated']]= df['Awards'].str.extract('Nominated for (\d+) (.*). Another', expand=True)


# In[54]:

df['AwardWon']= df['AwardWon'].apply(lambda x: strip_plural(x))
df['AwardNominated']= df['AwardNominated'].apply(lambda x: strip_plural(x))


# In[55]:

#drop all duplicate entries
df = df.drop_duplicates()
df1 = df[['imdbID','AwardWon','AwardCount']]
df1 = df1.pivot(index = 'imdbID', columns='AwardWon', values='AwardWon').drop(['nan'],1)
df1 = df1.add_suffix('_won') 


# In[56]:

df2 = df[['imdbID','AwardNominated','NominatedCount']]
df2 = df2.pivot(index = 'imdbID', columns='AwardNominated', values='AwardNominated').drop(['nan'],1)
df2 = df2.add_suffix('_nominated')


# In[57]:

df3 = pd.concat([df1,df2],axis =1)
df.head()


# In[59]:

df4 = df[['imdbID','Title','Awards','Awards_won','AwardCount','Awards_nominated','NominatedCount']].sort_values(by='imdbID')
df4.set_index('imdbID',inplace=True)
result_df = df4.join(df3, how='inner')
result_df.head()


# In[60]:

result_df = result_df.fillna(0)


# In[61]:

#calculate total awards won for each movie
result_df['Awards_won'] = result_df['Awards_won'].astype(int) + result_df['AwardCount'].astype(int)
#calculate total nominations
result_df['Awards_nominated'] = result_df['Awards_nominated'].astype(int) + result_df['NominatedCount'].astype(int)


# In[63]:

result_df = result_df.drop(['AwardCount','NominatedCount'], axis =1)   
result_df.head()


# In[67]:

result_df.to_csv('Ques04.csv',sep=',', index=False)


# In[ ]:



