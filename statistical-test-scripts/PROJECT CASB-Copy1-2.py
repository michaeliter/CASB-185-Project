#!/usr/bin/env python
# coding: utf-8

# In[24]:



import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import Image
import matplotlib.pyplot as plt 
from scipy.stats import linregress
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from PIL import Image 


# In[22]:


#this code was adpated from what was learned in LS40
def BigBox (group1, group2,Country_name):
    #make an array of the data 
    A = np.array(group1)
    B = np.array(group2)
    #count the amount of datapoints in the groups
    n1 = len(group1)
    n2 = len(group2)
    differenceMedian = np.median(B) - np.median(A) 
    population = np.concatenate([group1, group2]) # Make Big Box model by combining the dataset
    sims = []
    #calculate the difference in medians between the groups at each iterated

    for i in range(10000):
        sim_group1 = np.random.choice(population,n1)
        sim_group2 = np.random.choice(population,n2)
        sims.append(np.median(sim_group2)-np.median(sim_group1)) # Calculate difference of medians for each sample

    posLimit = abs(differenceMedian)
    negLimit = -1*posLimit
    # then a histogram was created for the data

    p = sns.displot(sims,kde=False)
    p.set(xlabel="Difference in Medians", ylabel="Count", title = "Null Distribution with Observed Difference in Median of" + Country_name);
    
    # Calculate  p-value
    differenceMedian = np.round(differenceMedian,3)
    extreme = sum(sims >= posLimit) + sum(sims <= negLimit)
    pvalue = extreme/10000
    print("The observed difference in medians is",differenceMedian)
    print ("The p-value is",pvalue)


# In[23]:


#file path to the csv for Portugal
#then the function is called for Portugal
#the calculated p-val is outputted
#pval  was 0.0
spreadsheet = pd.read_csv("/Users/daljit/Downloads/portugal_excess_deaths.csv")   
BigBox(spreadsheet["covid_deaths"],spreadsheet["excess_deaths"], "Portugal")


# In[18]:


#file path to the csv for USA
#then the function is called for USA
#the calculated p-val is outputted
#pval  was 0.0
data="/Users/daljit/Downloads/united_states_excess_deaths.csv"
spreadsheet = pd.read_csv("/Users/daljit/Downloads/united_states_excess_deaths.csv")
BigBox(spreadsheet["covid_deaths"],spreadsheet["excess_deaths"],"USA")


# In[19]:


#file path to the csv for Mexico
#then the function is called for Mexico
#the calculated p-val is outputted
#pval  was 0.4038
spreadsheet = pd.read_csv("/Users/daljit/Downloads/mexico_excess_deaths.csv")
BigBox(spreadsheet["covid_deaths"],spreadsheet["excess_deaths"],"Mexico")


# In[20]:


#file path to the csv for Italy
#then the function is called for Italy
#the calculated p-val is outputted
#pval  was 0.0
data="/Users/daljit/Downloads/italy_deaths.csv"
spreadsheet = pd.read_csv("/Users/daljit/Downloads/italy_excess_deaths.csv")
BigBox(spreadsheet["covid_deaths"],spreadsheet["excess_deaths"],"Italy")


# In[21]:


#file path to the csv for South Africa
#then the function is called for South Africa
#the calculated p-val is outputted
#pval  was 0.0
data="/Users/daljit/Downloads/south_africa_deaths.csv"
spreadsheet = pd.read_csv("/Users/daljit/Downloads/south_africa_excess_deaths.csv")
BigBox(spreadsheet["covid_deaths"],spreadsheet["excess_deaths"],"South Africa")


# In[22]:


#file path to the csv for South Korea
#then the function is called for South Korea
#the calculated p-val is outputted
#pval  was 0.0087
spreadsheet = pd.read_csv("/Users/daljit/Downloads/south_korea_excess_deaths.csv")
BigBox(spreadsheet["covid_deaths"],spreadsheet["excess_deaths"],"South Korea")


# In[ ]:




