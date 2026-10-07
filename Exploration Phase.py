#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_excel(r"D:\البومي\EXCEL\Gaming Exp Rating Analysis\Game Rating Dataset+.xlsx")
df


# # Dataset Cleaning

# In[5]:


df = df.dropna(how= 'all',axis=1)
df


# In[6]:


df.columns = df.columns.str.strip()
df


# In[7]:


df = df.dropna(subset=['Game Name'])
df


# In[8]:


df = df = df.drop(columns=['Unnamed: 24','Unnamed: 25','Unnamed: 26'])
df


# In[15]:


df['Year played'] = df['Year played'].astype(int)
df['Status'] = df['Status'].str.strip()
df


# # Dataset Overview

# In[16]:


df.info()


# In[17]:


df.describe()


# # Categorical Distributions & Ranking Breakdown

# My Game Rank Breakdown

# In[18]:


df['My_Rate'].value_counts()


# Completion Status

# In[19]:


df['Status'].value_counts()


# Game Type

# In[20]:


df['Type'].value_counts()


# Game Genres

# In[23]:


df['Genres'].value_counts()


# # Rating Correlations & Analysis

# General Correlation

# In[24]:


df.corr()


# Best Games acording to Avg_rating

# In[30]:


df[['Game Name', 'My_Rate', 'Avg_rating', 'MY_Rating_Game_Rank']].sort_values(by='Avg_rating', ascending=False).head(10)


# # Exploring Visualy

# In[ ]:


plt.figure(figsize=(20, 10))


# Game Rank Distribution

# In[45]:


plt.figure(figsize=(20, 10))
plt.subplot(2,2,1)
ax = sns.countplot(
    data=df, 
    y='MY_Rating_Game_Rank', 
    order=df['MY_Rating_Game_Rank'].value_counts().index,
    palette='magma'
)
plt.xlabel('Count', fontsize=12)
plt.ylabel('MY_Rating_Game_Rank', fontsize=12)
plt.title('Distribution of Game Ranks')
ax.bar_label(ax.containers[0], padding=3)
plt.tight_layout()
plt.show()


# Rating Score Distribution

# In[46]:


plt.figure(figsize=(20, 10))
plt.subplot(2,2,2)
sns.kdeplot(df['My_Rate'], label='My_Rate', fill=True)
sns.kdeplot(df['Avg_rating'], label='Avg_rating', fill=True)
plt.title('My Rate vs Average Rating Density')
plt.legend()
plt.show()


# Correlation Heatmap

# In[51]:


rating_cols = ['My_Rate', 'IGN Rating (/10)', 'Steam Rating (/10)', 'Metacritic Rating (/10)', 'Avg_rating']
correlation_matrix = df[rating_cols].corr()
plt.figure(figsize=(20, 10))
plt.subplot(2,2,3)
sns.heatmap(correlation_matrix, annot= True,cmap='coolwarm', fmt ='.2f', vmin=0, vmax=1)
plt.title('Rating_Correlations')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




