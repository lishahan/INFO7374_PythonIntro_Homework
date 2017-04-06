
# coding: utf-8

# # Q2_PART TWO
# EMPLOYEE COMPENSATION ANALYSIS

# Use 'employee_compensation' data set.
# • Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# • Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# • For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# • Display the top 5 Job Families according to this percentage value using df.head().
# • Write the output (jobs and percentage value) to a csv.

# In[1]:

import pandas as pd
from pandas import Series, DataFrame
import numpy as np


# In[2]:

path_local='Data/employee_compensation.csv'
data_raw = pd.read_csv(path_local)


# ### Process raw data: keep useful columns

# In[4]:

df1=data_raw.loc[:,['Job Family','Employee Identifier','Salaries','Overtime','Total Benefits','Total Compensation']]


# ### Group salaries and overtime by unique employee id, caculate its average and put in different data frames

# In[41]:

frame1 = DataFrame(df1['Salaries'].groupby([df1['Employee Identifier']]).mean(),columns=['Salaries'])
frame2 = DataFrame(df1['Overtime'].groupby([df1['Employee Identifier']]).mean(),columns=['Overtime'])


# ### Concate data frames of salaries and overtime

# In[50]:

frame_overtime=pd.concat([frame1,frame2],axis=1)
frame_overtime['Percent'] = frame_overtime['Overtime']/frame_overtime['Salaries']


# In[57]:

frame_overtime['Employee'] = frame_overtime.index


# ### Group employees by overtime salaries is over 5% of salaires

# In[61]:

group = frame_overtime['Employee'].groupby([frame_overtime['Percent']>0.05])


# ### Count number of employees whoes overtime salaires is 5% over salaries

# In[79]:

print('There are ',group.size()[True], ' employees overtime salaries is over 5% of salaries')


# ### Group total benefit and compensation by unique job family, caculate its average and put in different data frames

# In[80]:

frame3 = DataFrame(df1['Total Benefits'].groupby([df1['Job Family']]).mean(),columns=['Total Benefits'])
frame4 = DataFrame(df1['Total Compensation'].groupby([df1['Job Family']]).mean(),columns=['Total Compensation'])


# ### Concate data frames of total benefits and compensation

# In[83]:

frame_jobfamily=pd.concat([frame3,frame4],axis=1)
frame_jobfamily['Percent_Total_Benefit']=frame3['Total Benefits']/frame4['Total Compensation']


# ### A little sample

# In[84]:

frame_jobfamily.head()


# ### Export data to csv file

# In[88]:

frame_jobfamily.to_csv('Q2_p2.csv')


# In[ ]:



