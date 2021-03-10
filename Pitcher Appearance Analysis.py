#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
pd.options.display.max_rows = 200
pd.options.display.max_rows = 200
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


data = pd.read_excel(r'Sample Appearance.xlsx')
data.info()
data = data.infer_objects()


# In[12]:


df = data[:-1]


# In[13]:


df['Fastball'].sum()


# In[14]:


plt.figure()
sns.barplot(x='Pitches', y='Hits', data = df, orient = 'l')


# In[15]:


plt.figure()
sns.barplot(x='Pitches', y='Fastball.1', data = df, orient = 'l')


# Pitch Breakdown

# In[16]:


TotalFB = df['Fastball'].sum()
TotalCB = df['Curve'].sum()
TotalCH = df['Change'].sum()
TotalSL = df['Slider'].sum()
TotalOther = df['Other'].sum()


# In[17]:


PieData = [TotalFB, TotalCB, TotalCH, TotalSL, TotalOther]


# In[18]:


labels = 'Fastball', 'Curveball', 'Changeup', 'Slider', 'Other' 
fig = plt.figure(figsize =(10, 7)) 
plt.pie(PieData, labels = labels) 

plt.show() 


# In[19]:


df.Hits.sum()


# In[ ]:





# In[20]:


Pitches = df['Pitches']
FastVelo = df['Fastball.1']
  
plt.plot(Pitches, FastVelo, color='red', marker='o')
plt.title('Velocity Per Pitch Interval', fontsize=14)
plt.xlabel('Pitch Interval', fontsize=14)
plt.ylabel('Fastball Velocity', fontsize=14)
plt.grid(True)
plt.show()


# In[21]:


Pitches = df['Pitches']
CurveVelo = df['Curve.1']
  
plt.plot(Pitches, CurveVelo, color='red', marker='o')
plt.title('Curve Velocity Per Pitch Interval', fontsize=14)
plt.xlabel('Pitch Interval', fontsize=14)
plt.ylabel('Curveball Velocity', fontsize=14)
plt.grid(True)
plt.show()


# In[22]:


Pitches = df['Pitches']
ChangeVelo = df['Change.1']
  
plt.plot(Pitches, ChangeVelo, color='red', marker='o')
plt.title('Change Velocity Per Pitch Interval', fontsize=14)
plt.xlabel('Pitch Interval', fontsize=14)
plt.ylabel('Change Velocity', fontsize=14)
plt.grid(True)
plt.show()


# In[23]:


Pitches = df['Pitches']
SliderVelo = df['Slider.1']
  
plt.plot(Pitches, SliderVelo, color='red', marker='o')
plt.title('Slider Velocity Per Pitch Interval', fontsize=14)
plt.xlabel('Pitch Interval', fontsize=14)
plt.ylabel('Slider Velocity', fontsize=14)
plt.grid(True)
plt.show()


# In[24]:


Pitches = df['Pitches']
OtherVelo = df['Other.1']
  
plt.plot(Pitches, OtherVelo, color='red', marker='o')
plt.title('Other Velocity Per Pitch Interval', fontsize=14)
plt.xlabel('Pitch Interval', fontsize=14)
plt.ylabel('Slider Velocity', fontsize=14)
plt.grid(True)
plt.show()


# In[ ]:




