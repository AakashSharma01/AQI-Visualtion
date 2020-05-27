#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker


get_ipython().run_line_magic('matplotlib', 'inline')


# In[82]:


os.getcwd()


# In[83]:


os.chdir('C:\\Users\\asus\\Desktop\\Online Courses\\Applied Machine Learning Using Python Univ of Michigan\\Course 2_Plotting & Charting\\Assignment 4')


# In[84]:


Delhi = pd.read_csv(r'C:\Users\asus\Desktop\Online Courses\Applied Machine Learning Using Python Univ of Michigan\Course 2_Plotting & Charting\Assignment 4\Delhi AQI 2020.csv')


# In[86]:


AnnArbor = pd.read_csv(r'C:\Users\asus\Desktop\Online Courses\Applied Machine Learning Using Python Univ of Michigan\Course 2_Plotting & Charting\Assignment 4\ad_aqi_tracker_data.csv')


# In[87]:


Delhi['Date'] = pd.to_datetime(Delhi['Date'], format = '%m/%d/%Y')
AnnArbor['Date'] = pd.to_datetime(AnnArbor['Date'], format = '%m/%d/%Y')
AnnArbor.head()


# In[88]:


# Create figure and plot space
fig, ax = plt.subplots(figsize=(8, 6))

# Add x-axis and y-axis
ax.plot('Date', 'PM2.5', data=Delhi,color='lightcoral', linewidth=1)
ax.plot('Date', 'PM2.5 AQI Value', data=AnnArbor,color='skyblue', linewidth=1)

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="PM2.5 AQI Value",
       title="PM2.5 AQI Value in Delhi & Ann Arbour(2020)")

plt.legend(['Delhi','Ann Arbor'],loc=0,frameon=False)

# Define the date format
date_form = DateFormatter("%m-%d-%y")
ax.xaxis.set_major_formatter(date_form)

# Ensure a major tick for each week using (interval=1) 
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
_=plt.xticks(rotation=90)  
plt.show()


# In[ ]:




