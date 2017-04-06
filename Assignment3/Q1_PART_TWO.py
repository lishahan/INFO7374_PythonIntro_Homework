
# coding: utf-8

# # Q1_PART TWO
# NYC VEHICLE COLLISION ANALYSIS

# Use ‘vehicle_collisions’ data set.
# • For each borough, find out distribution of each collision scale. (One car
# involved? Two? Three? or more?) (From 2015 to present)
# • Display a few rows of the output use df.head().
# • Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

# In[206]:

import pandas as pd
from pandas import Series, DataFrame
import numpy as np


# In[207]:

path_local='Data/vehicle_collisions.csv'
data_raw = pd.read_csv(path_local)


# ### Process raw data: keep only columns of borough and vehichle 1~5 type

# In[219]:

df1=data_raw.loc[:,['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]


# ### Replace nan with not specified

# In[220]:

df2=df1.replace(np.nan,'NOT SPECIFIED')


# ### Get list of viehcle 1~5 type

# In[221]:

arr_vieh1 = df2['VEHICLE 1 TYPE'].unique()
arr_vieh2 = df2['VEHICLE 2 TYPE'].unique()
arr_vieh3 = df2['VEHICLE 3 TYPE'].unique()
arr_vieh4 = df2['VEHICLE 4 TYPE'].unique()
arr_vieh5 = df2['VEHICLE 5 TYPE'].unique()
list_vieh = arr_vieh1.tolist()+arr_vieh2.tolist()+arr_vieh3.tolist()+arr_vieh4.tolist()+arr_vieh5.tolist()
list_vieh.remove('NOT SPECIFIED')


# ### Replace not specified with 0, others with 1

# In[225]:

df3=df2.replace('NOT SPECIFIED',int(0))
df4=df3.replace(list_vieh,int(1))
df4['BOROUGH']=df4['BOROUGH'].replace(0,'NOT SPECIFIED')


# ### Group vehicle 1~5 type by borough

# In[246]:

group1= df4['VEHICLE 1 TYPE'].groupby([df4['BOROUGH']])
group2= df4['VEHICLE 2 TYPE'].groupby([df4['BOROUGH']])
group3= df4['VEHICLE 3 TYPE'].groupby([df4['BOROUGH']])
group4= df4['VEHICLE 4 TYPE'].groupby([df4['BOROUGH']])
group5= df4['VEHICLE 5 TYPE'].groupby([df4['BOROUGH']])


# ### For each borough, find out distribution of each collision scale

# In[247]:

frame1=DataFrame(group1.sum()-group2.sum(),columns=['ONE_VEHICLE_INVOLVED'])
frame1['TWO_VEHICLE_INVOLVED']=DataFrame(group2.sum()-group3.sum())
frame1['THREE_VEHICLE_INVOLVED']=DataFrame(group3.sum()-group4.sum())
frame1['MORE_VEHICLE_INVOLVED']=DataFrame(group4.sum())
del frame1.index.name
frame1.columns.name='BOROUGH'


# In[248]:

frame1


# ### Put data to csv file

# In[250]:

frame1.to_csv('Q1_p2.csv', index_label='BOROUGH')


# In[ ]:




# In[ ]:



