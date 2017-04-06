
# coding: utf-8

# # Q3_PART ONE
# CRICKET MATCHES ANALYSIS

#  Use ‘cricket_matches’ data set.
#  • Calculate the average score for each team which host the game and win the game.
#  • Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
#  • Display a few rows of the output use df.head()
#  • Generate a csv output

# In[1]:

import pandas as pd
from pandas import Series, DataFrame


# In[3]:

path_local='Data/cricket_matches.csv'
data_raw = pd.read_csv(path_local)


# ### Keep only the rows that who is the host and also the winner

# In[9]:

df=data_raw[data_raw.home==data_raw.winner]


# ### A function to get the score of each winner

# In[24]:

def get_score(x):
    if x['winner']==x['innings1']:
        x['Score']=x['innings1_runs']
    else:
        x['Score']=x['innings2_runs']
    return x


# ### Get scores of all winners

# In[28]:

df=df.apply(lambda x: get_score(x),axis=1)


# ### Group scores by home and calulate mean score of each team

# In[32]:

group=df.groupby(['home'])['Score']


# In[33]:

frame=DataFrame(group.mean())


# ### A little sample

# In[35]:

frame.head()


# ### Generate a csv output

# In[115]:

frame.to_csv('Q3_p1.csv')


# In[ ]:



