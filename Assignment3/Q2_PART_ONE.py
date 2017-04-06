
# coding: utf-8

# # Q2_PART ONE
# EMPLOYEE COMPENSATION ANALYSIS

# • Use 'employee_compensation' data set.
# • Find out the highest paid departments in each organization group by
# calculating mean of total compensation for every department.
# • Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# • Display a few rows of the output use df.head().
# • Generate a csv output.

# In[1]:

import pandas as pd
from pandas import Series, DataFrame


# In[2]:

path_local='Data/employee_compensation.csv'
data_raw = pd.read_csv(path_local)


# ### Process raw data: keep useful columns

# In[3]:

df=data_raw.loc[:,['Total Compensation','Organization Group', 'Department']]


# ### Group total compensation by organization and its departement, caculate average compensation

# In[9]:

frame=DataFrame(df.groupby(['Organization Group', 'Department'])['Total Compensation'].mean())


# In[11]:

frame0=frame.reset_index()


# ### Sorting compensation of each department in each organization

# In[12]:

frame1=frame0.sort_values(['Organization Group','Total Compensation'],ascending=[True,False])


# ### A little sample

# In[13]:

frame1.head()


# ### Export data to csv file

# In[46]:

frame1.to_csv('Q2_p1.csv')


# In[ ]:



