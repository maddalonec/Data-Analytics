#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_rows = 200
pd.options.display.max_rows = 200
import matplotlib.pyplot as plt
import seaborn as sns

import os 
import folium
from folium import plugins
import rasterio as rio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import earthpy as et
from geopy.geocoders import Nominatim


# In[2]:


data = pd.read_excel(r'California.xls')
data.info()
data = data.infer_objects()


# In[ ]:





# In[3]:


# Sort by Population
df = data.sort_values(by='Population', ascending= False)


# In[4]:


# New Column for Crime Rate
df["Violent Crime Rate"] = df["Violent\ncrime"]/df['Population']


# In[5]:


# New Column for Murder Rate
df["Murder Rate"] = df["Murder and\nnonnegligent\nmanslaughter"]/df['Population']


# In[6]:


# New Column for Total Crime
df["Total Crime"] = df["Violent\ncrime"]+df['Property\ncrime']


# In[7]:


# New Column for Total Crime Rate
df["Total Crime Rate"] = df["Total Crime"]/df['Population']


# In[8]:


#Data Frame for top ten most populated cities
df10 =df.head(10)


# In[9]:


#Data Frame for top 50 most populated cities
df50 =df.head(50)


# In[10]:


#City with the Most Robberies
df[df['Robbery'] == df.Robbery.max()]


# In[11]:


#City with the highest crime rate
df[df['Violent Crime Rate'] == df['Violent Crime Rate'].max()]
dfViolentRate = df.sort_values(by='Violent Crime Rate', ascending= False)
dfViolentRate =dfViolentRate.head(25)
dfViolentRate


# In[12]:


#ten Largest cities
df10


# In[13]:


StateMurderRate = (df['Murder and\nnonnegligent\nmanslaughter'].sum())/(df['Population'].sum())
StateMurderRate


# In[14]:


StateViolentCrimeRate = (df['Violent\ncrime'].sum())/(df['Population'].sum())
StateViolentCrimeRate


# In[15]:


# Scatter Plot Showing Cities Above State Crime Rate
x = df10.Population
y = df10['Violent\ncrime']
plt.figure()
sns.scatterplot(x='Population', y='Violent\ncrime', data=df10, hue = "City")
plt.plot(x, x*StateViolentCrimeRate, linestyle='solid')


# In[16]:


#underperforming cities on crime
dfWorstRate = df[df['Violent Crime Rate'] > StateViolentCrimeRate].sort_values(by='Violent Crime Rate', ascending= False)
dfWorstRate


# In[17]:


plt.figure()
sns.regplot(data=df, x="Population", y="Violent\ncrime")


# In[ ]:





# In[18]:


cityPop = pd.crosstab(df10.Population, df10['City'])


# In[19]:



plt.figure()
sns.barplot(x='Population', y='City', data=df10, orient='h')


# In[20]:


plt.figure()
sns.barplot(x='Violent Crime Rate', y='City', data=df10, orient='h')


# In[21]:


df10['City'] = df10['City']+' USA'


# In[22]:


geolocator = Nominatim(user_agent="example")


# In[23]:


l = {'CITY': df10['City'],
    'VIOLENT': df10['Violent\ncrime']}

l['COORDS'] = []
for k in l['CITY']:
    loc = geolocator.geocode(k).raw
    l['COORDS'].append((loc['lat'], loc['lon']))

df2 = pd.DataFrame(l)
state_map = folium.Map(location = [36.7783, -119.4179], zoom_start=6)
for i,r in df2.iterrows():
    folium.Marker(location=r['COORDS'],
                  popup = ("Violent Crimes", r['VIOLENT']),
                  tooltip= r['CITY']).add_to(state_map)
state_map


# In[24]:


l = {'CITY': df10['City'],
    'VIOLENT': df10['Violent\ncrime'],
    'VIOLENTRATE': df10['Violent Crime Rate']
    }

l['COORDS'] = []
for k in l['CITY']:
    loc = geolocator.geocode(k).raw
    l['COORDS'].append((loc['lat'], loc['lon']))

df2 = pd.DataFrame(l)
state_map = folium.Map(location = [36.7783, -119.4179], zoom_start=6)
for i in range(0,len(df2)):
   folium.Circle(
      location= df2.iloc[i]['COORDS'],
      popup= ("Violent Crimes: "+ "{:1}".format(df2.iloc[i]['VIOLENT'])),
      tooltip= df2.iloc[i]['CITY'],
      radius=df2.iloc[i]['VIOLENT']*7.00,
      color='crimson',
      fill=True,
      fill_color='crimson'
   ).add_to(state_map)

state_map


# In[25]:


l


# In[26]:


l = {'CITY': df10['City'],
    'VIOLENT': df10['Violent\ncrime'],
    'VIOLENTRATE': df10['Violent Crime Rate']
    }

l['COORDS'] = []
for k in l['CITY']:
    loc = geolocator.geocode(k).raw
    l['COORDS'].append((loc['lat'], loc['lon']))

df2 = pd.DataFrame(l)
state_map2 = folium.Map(location = [36.7783, -119.4179], zoom_start=6)
for i in range(0,len(df2)):
   folium.Circle(
      location= df2.iloc[i]['COORDS'],
      popup=("Violent Crime Rate: "+" {:.4%}".format(df2.iloc[i]['VIOLENTRATE'])),
      tooltip= df2.iloc[i]['CITY'],
      radius=df2.iloc[i]['VIOLENTRATE']*700000.00,
      color='green',
      fill=True,
      fill_color='green'
   ).add_to(state_map2)

state_map2


# In[27]:


l = {'CITY': df10['City'],
    'MURDERS': df10["Murder and\nnonnegligent\nmanslaughter"],
    }

l['COORDS'] = []
for k in l['CITY']:
    loc = geolocator.geocode(k).raw
    l['COORDS'].append((loc['lat'], loc['lon']))

df2 = pd.DataFrame(l)
state_map3 = folium.Map(location = [36.7783, -119.4179], zoom_start=6)
for i in range(0,len(df2)):
   folium.Circle(
      location= df2.iloc[i]['COORDS'],
      popup= ("Murders: "+ "{:1}".format(df2.iloc[i]['MURDERS'])),
      tooltip= df2.iloc[i]['CITY'],
      radius=df2.iloc[i]['MURDERS']*500.00,
      color='blue',
      fill=True,
      fill_color='blue'
   ).add_to(state_map3)

state_map3


# In[28]:


l = {'CITY': df10['City'],
    'MRATE': df10['Murder Rate']
    }

l['COORDS'] = []
for k in l['CITY']:
    loc = geolocator.geocode(k).raw
    l['COORDS'].append((loc['lat'], loc['lon']))

df2 = pd.DataFrame(l)
state_map4 = folium.Map(location = [36.7783, -119.4179], zoom_start=6)
for i in range(0,len(df2)):
   folium.Circle(
      location= df2.iloc[i]['COORDS'],
      popup=("{:}".format(df2.iloc[i]['CITY']) + " Murder Rate: "+" {:.6%}".format(df2.iloc[i]['MRATE'])),
       tooltip= df2.iloc[i]['CITY'],
      radius=df2.iloc[i]['MRATE']*250000000.00,
      color='yellow',
      fill=True,
      fill_color='yellow'
   ).add_to(state_map4)

state_map4


# In[29]:


l = {'CITY': df10['City'],
    'TOTAL': df10['Total Crime'],
    }

l['COORDS'] = []
for k in l['CITY']:
    loc = geolocator.geocode(k).raw
    l['COORDS'].append((loc['lat'], loc['lon']))

df2 = pd.DataFrame(l)
state_map5 = folium.Map(location = [36.7783, -119.4179], zoom_start=6)
for i in range(0,len(df2)):
   folium.Circle(
      location= df2.iloc[i]['COORDS'],
      popup= ("Total Crimes: "+ "{:1}".format(df2.iloc[i]['TOTAL'])),
       tooltip= df2.iloc[i]['CITY'],
      radius=df2.iloc[i]['TOTAL']*3.00,
      color='purple',
      fill=True,
      fill_color='purple'
   ).add_to(state_map5)

state_map5


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




