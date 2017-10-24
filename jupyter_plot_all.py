
# coding: utf-8

# In[36]:


get_ipython().magic(u'matplotlib inline')

func = lambda x: 100*x.count()/df.shape[0]

import glob
import os

import pandas as pd

path = '/tmp/'                     # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent


df_from_each_file = (pd.read_csv(f) for f in all_files)
df   = pd.concat(df_from_each_file, ignore_index=True)

#df = pd.read_csv('/tmp/word_difficulty.csv')
ax = df.pivot_table(values='word', index='difficulty',  columns='author',  aggfunc=len).plot(kind='line', legend = True)
ax.set_ylabel("Percentage of Total Words")
ax.set_xlabel("Word Difficulty")

import matplotlib.pyplot as plt
axes = plt.gca()
#axes.set_ylim([0, 30])

df.columns


# In[20]:


df.pivot_table(values='word', index='difficulty',  columns='author',  aggfunc=len)


# In[33]:


a = df.pivot_table(values='word', index='difficulty',  columns='author',  aggfunc=len)
a.columns
cols = [u'Clinton', u'Michal', u'Trump']
a[cols] = a[cols].div(a[cols].sum(axis=0), axis=1).multiply(100)


# In[55]:


import matplotlib
matplotlib.rc('legend', fontsize=30, handlelength=2)
ax = a.plot(kind='line', legend = True, figsize=(15,10), fontsize=20)
ax.set_ylabel("Percentage of Total Words")
ax.set_xlabel("Word Difficulty")
