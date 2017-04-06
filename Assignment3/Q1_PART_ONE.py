
# coding: utf-8

# # Q1_PART ONE
# NYC VEHICLE COLLISION ANALYSIS

# Use ‘vehicle_collisions’ data set.
# • For each month in 2016, find out the percentage of collisions in
# Manhattan out of that year's total accidents in New York City.
# • Display a few rows of the output use df.head().
# • Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[2]:

import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime,date


# In[3]:

path_local='Data/vehicle_collisions.csv'
data_raw = pd.read_csv(path_local)


# ### Process raw data: only keep date and borough columns

# In[8]:

df1=data_raw.loc[:,['DATE','BOROUGH']]


# ### Extract year and month from date column and put year and month in new columns

# In[10]:

df1.loc[df1.index,'YEAR']=df1.loc[df1.index,'DATE'].apply(lambda x: datetime.strptime(x,'%m/%d/%y').date().strftime('%y'))
df1['MONTH']=df1['DATE'].apply(lambda x: datetime.strptime(x,'%m/%d/%y').date().strftime('%b'))


# ### Only keep data in year 2016

# In[11]:

df1=df1[df1['YEAR']=='16']


# ### Get accident information only for Manhattan

# In[13]:

df0=df1.loc[df1['BOROUGH'] == 'MANHATTAN']


# ### Group accident happended in NYC and Manhattan by month

# In[29]:

group = df1.groupby(df1['MONTH'])['BOROUGH']
group1 = df0.groupby(df0['MONTH'])['BOROUGH']


# ### Count the total accidents in NYC and Manhattan and create data frame for the two boroughs

# In[37]:

series=group.size()
series1=group1.size()


# In[38]:

del series1.index.name
df2=DataFrame(series1,columns=['MANHATTAN'])
df2.columns.name='MONTH'


# In[39]:

del series.index.name
df3=DataFrame(series,columns=['NYC'])
df3.columns.name='MONTH'


# ### Concate data frames of NYC and Manhattan, reindexing and caculate percentage

# In[40]:

result=pd.concat([df2,df3],axis=1)


# In[41]:

frame=result.reindex(index=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])


# In[42]:

frame['PERCENTAGE']=frame['MANHATTAN']/frame['NYC']


# ### A little sample

# In[43]:

frame


# ### Put result in csv file

# In[407]:

frame.to_csv('Q1_p1.csv', index_label='MONTH')


# In[ ]:



