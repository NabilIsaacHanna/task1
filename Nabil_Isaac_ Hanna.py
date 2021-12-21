# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:28:55 2021

@author: Nabil_Isaac8cf
"""
import pandas as pd
 #import pandas package to read dataset 
dataset= pd.read_csv("Wuzzuf_Jobs.csv")
 #making data frame
dataset.head()
 #descripe dataset and summery
dataset.describe()

import pandas as pd
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.drop_duplicates(keep="first", inplace= True)
#subset= choose the column
# keep= choose the value tou keep
#removes rows with duplicates if True
dataset.isnull()
#show the null values(boolean)
dataset
#show dataset

import pandas as pd
import matplotlib.pyplot as plt
dataset= pd.read_csv("Wuzzuf_Jobs.csv")
comps = dataset["Company"].value_counts()
#count values of the column called company
comps
#show comps
label = comps[:7].index
value = comps[:7].values
plt.pie(value,labels=label)
plt.title("the most demanding companies for jobs")
plt.show()


common_job=dataset["Title"].value_counts()
common_job
#show the most common job  title
label=common_job[:9].index
value=common_job[:9].values
plt.bar(label , value, color="blue")
plt.title("the Most Common job")
plt.xlabel("jobs")
plt.ylabel("number of job selection")
plt.show()

area =dataset["Location"].value_counts()
area

index = area[:6].index
values = area[:6].values
plt.bar(index , values, width=0.4 , color = "green")
plt.title("the most popular areas")
plt.show()



skill =dataset["Skills"].str.cat(sep =",")
skills =pd.Series (skill.split(",")).value_counts()
skills
labels = skills.index[:7]
values = skills.values [:7]
plt.bar (labels ,values , width= 0.5 , color= "orange")
plt.title("The Most Popular Skills")
plt.show()