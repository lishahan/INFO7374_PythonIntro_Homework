
# coding: utf-8

# # Q4_PART ONE
# MOVIE AWARDS ANALYSIS

# Use ‘movies_awards’ data set.
# • You are supposed to extract data from the awards column in this dataset and split it into several
# columns. An example is given below.
# • The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# • You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
# • If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
# • Create two separate columns for each award category (won and nominated).
# • Write your output to a csv file.

# In[25]:

import pandas as pd
import re


# In[26]:

path_local='Data/movies_awards.csv'
data_raw = pd.read_csv(path_local)


# ### Process raw data: only keep Awards column and drop nan from Awards

# In[27]:

df1=data_raw.loc[:,['Awards']]
df1=df1[df1.Awards.notnull()]


# ### functions for filtering win and nomination and awards

# In[78]:

def get_win(x):
    rex='(\d+) win'
    rex1='(\d+) won'
    l=re.findall(rex,x)
    l1=re.findall(rex1,x)
    a=0
    if l1!=[]:
        if l==[]:
            a+=int(l1[0])
        else:
            a=a + int(l1[0]) + int(l[0])
    else:
        if l==[]:
            a+=0
        else:
            a += int(l[0])
    return a


# In[89]:

def get_nom(x):
    rex='(\d+) nom'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a      


# In[122]:

def get_prime_nom(x):
    rex='Nominated for (\d+) Prime'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a 


# In[107]:

def get_oscar_nom(x):
    rex='Nominated for (\d+) Oscar'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a 


# In[112]:

def get_golden_nom(x):
    rex='Nominated for (\d+) Golden'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a 


# In[124]:

def get_BAFTA_nom(x):
    rex='Nominated for (\d+) BAFTA'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a 


# In[125]:

def get_prime_win(x):
    rex='Won (\d+) Prime'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a


# In[126]:

def get_oscar_win(x):
    rex='Won (\d+) Oscars'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a


# In[127]:

def get_golden_win(x):
    rex='Won (\d+) Golden'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a


# In[117]:

def get_BAFTA_win(x):
    rex='Won (\d+) BAFTA'
    l=re.findall(rex,x)
    a=0
    if l!=[]:
        a += int(l[0])
    else:
        a+=0
    return a


# ### Create new columns for each kind of award

# In[128]:

df1['Awards_won']=df1['Awards'].apply(lambda x: get_win(x))
df1['Awards_nominated']=df1['Awards'].apply(lambda x: get_nom(x))
df1['Prime_Awards_nominated']=df1['Awards'].apply(lambda x: get_prime_nom(x))
df1['Oscar_Awards_nominated']=df1['Awards'].apply(lambda x: get_oscar_nom(x))
df1['Golden_Globe_Awards_nominated']=df1['Awards'].apply(lambda x: get_golden_nom(x))
df1['BAFTA_Awards_nominated']=df1['Awards'].apply(lambda x: get_BAFTA_nom(x))
df1['Prime_Awards_won']=df1['Awards'].apply(lambda x: get_prime_win(x))
df1['Oscar_Awards_won']=df1['Awards'].apply(lambda x: get_oscar_win(x))
df1['Golden_Globe_Awards_won']=df1['Awards'].apply(lambda x: get_golden_win(x))
df1['BAFTA_Awards_won']=df1['Awards'].apply(lambda x: get_BAFTA_win(x))


# ### A little sample

# In[129]:

df1.head()


# ### Write output to a csv file

# In[130]:

df1.to_csv('Q4_p1.csv')


# In[ ]:



