#!/usr/bin/env python
# coding: utf-8

# In[4]:



import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import Image
import matplotlib.pyplot as plt 
from scipy.stats import linregress
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from PIL import Image 


# In[60]:


data="/Users/daljit/Downloads/united_states_excess_deaths.csv"

CD = spreadsheet["covid_deaths"]
UD = spreadsheet["excess_deaths"]

# create violin plot
data = [CD, UD]
fig, ax = plt.subplots()
colors = ['orange', 'blue']
parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)


for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])

# add legend
ax.legend(["Covid Deaths", "Excess Deaths"])

# set axis labels and title
ax.set_title('Covid Death vs Excess Death in USA')
ax.set_xlabel("Type of Deaths")
ax.set_ylabel("Deaths")
ax.set_yscale('log')

# show plot
plt.show()


# In[57]:



import matplotlib.pyplot as plt

# load data from CSV file
spreadsheet = pd.read_csv("/Users/daljit/Downloads/portugal_excess_deaths.csv") 
CD = spreadsheet["covid_deaths"]
UD = spreadsheet["excess_deaths"]

# create violin plot
data = [CD, UD]
fig, ax = plt.subplots()
colors = ['orange', 'blue']
parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)


for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])

# add legend
ax.legend(["Covid Deaths", "Excess Deaths"])

# set axis labels and title
ax.set_title('Covid Death vs Excess Death in Portugal')
ax.set_xlabel("Type of Deaths")
ax.set_ylabel("Deaths")
ax.set_yscale('log')

# show plot
plt.show()


# In[61]:


import matplotlib.pyplot as plt

# load data from CSV file
spreadsheet = pd.read_csv("/Users/daljit/Downloads/south_korea_excess_deaths.csv")
CD = spreadsheet["covid_deaths"]
UD = spreadsheet["excess_deaths"]

# create violin plot
data = [CD, UD]
fig, ax = plt.subplots()
colors = ['orange', 'blue']
parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)


for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])

# add legend
ax.legend(["Covid Deaths", "Excess Deaths"])

# set axis labels and title
ax.set_title('Covid Death vs Excess Death in South Korea')
ax.set_xlabel("Type of Deaths")
ax.set_ylabel("Deaths")
ax.set_yscale('log')

# show plot
plt.show()


# In[106]:


import matplotlib.pyplot as plt

# load data from CSV file
spreadsheet = pd.read_csv("/Users/daljit/Downloads/mexico_excess_deaths.csv")
CD = spreadsheet["covid_deaths"]
UD = spreadsheet["excess_deaths"]

# create violin plot
data = [CD, UD]
fig, ax = plt.subplots()
colors = ['orange', 'blue']
parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)


for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])

# add legend
ax.legend(["Covid Deaths", "Excess Deaths"])

# set axis labels and title
ax.set_title('Covid Death vs Excess Death in Mexico')
ax.set_xlabel("Type of Deaths")
ax.set_ylabel("Deaths")
ax.set_yscale('log')


# show plot
plt.show()


# In[45]:


import matplotlib.pyplot as plt

# load data from CSV file
spreadsheet =  pd.read_csv("/Users/daljit/Downloads/south_africa_excess_deaths.csv")
CD = spreadsheet["covid_deaths"]
UD = spreadsheet["excess_deaths"]

# create violin plot
data = [CD, UD]
fig, ax = plt.subplots()
colors = ['orange', 'blue']
parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)


for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])

# add legend
ax.legend(["Covid Deaths", "Excess Deaths"])

# set axis labels and title
ax.set_title('Covid Death vs Excess Death in South Africa')
ax.set_xlabel("Type of Deaths")
ax.set_ylabel("Deaths")
ax.set_yscale('log')

# show plot
plt.show()


# In[ ]:





# In[ ]:





# In[105]:


import matplotlib.pyplot as plt

# load data from CSV file
spreadsheet = pd.read_csv("/Users/daljit/Downloads/italy_excess_deaths.csv")
CD = spreadsheet["covid_deaths"]
UD = spreadsheet["excess_deaths"]

# create violin plot
data = [CD, UD]
fig, ax = plt.subplots()
colors = ['orange', 'blue']
parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)


for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])

# add legend
ax.legend(["Covid Deaths", "Excess Deaths"])

# set axis labels and title
ax.set_title('Covid Death vs Excess Death in Italy')
ax.set_xlabel("Type of Deaths")
ax.set_ylabel("Deaths")
ax.set_yscale('log')
# show plot
plt.show()


# In[ ]:




