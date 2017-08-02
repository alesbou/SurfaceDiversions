# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 15:07:31 2017

@author: alesbou
"""


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Working inside subdirectory
abspath = os.path.abspath(__file__)
absname = os.path.dirname(abspath)
os.chdir(absname)

data = pd.read_csv('c2vsimSurface.csv')
average = data.mean()

results = []
df = pd.DataFrame()
q5 = pd.DataFrame()
q25 = pd.DataFrame()
q50 = pd.DataFrame()
q75 = pd.DataFrame()
q95 = pd.DataFrame()
q5['year0'] = data.mean()*0
q25['year0']=data.mean()*0
q50['year0']=data.mean()*0
q75['year0']=data.mean()*0
q95['year0']=data.mean()*0

for i in np.arange(1,11):
    data2 = data.rolling(window=i,center=False).sum()
    name = "year%s" % i
    q5[name] = data2.quantile(0.05) - average*i
    q25[name]=data2.quantile(0.25) - average*i
    q50[name]=data2.quantile(0.5) - average*i
    q75[name]=data2.quantile(0.75) - average*i
    q95[name]=data2.quantile(0.95) - average*i
    data2 = data2.min()- average*i
    df[name]=data2[1:22] 
    
q5 = q5.transpose()
q5 = q5.convert_objects(convert_numeric=True)
q5 = q5.reset_index()

q25 = q25.transpose()
q25 = q25.convert_objects(convert_numeric=True)
q25 = q25.reset_index()

q50 = q50.transpose()
q50 = q50.convert_objects(convert_numeric=True)
q50 = q50.reset_index()

q75 = q75.transpose()
q75 = q75.convert_objects(convert_numeric=True)
q75 = q75.reset_index()

q95 = q95.transpose()
q95 = q95.convert_objects(convert_numeric=True)
q95 = q95.reset_index()

df = df.transpose()
df = df.convert_objects(convert_numeric=True)
df = df.reset_index()

#Plotting
plt.style.use('ggplot')
plt.plot(np.arange(0,11),q50.r15, color='black',linewidth=2, label='Median')
plt.plot(np.arange(0,11),q5.r15, color='red',linewidth=1,ls='-.',label='Percentile 5')
plt.plot(np.arange(0,11),q95.r15, color='red',linewidth=1,ls='--',label='Percentile 95')
plt.plot(np.arange(0,11),q25.r15, color='blue',linewidth=1,ls='-.', label='Percentile 25')
plt.plot(np.arange(0,11),q75.r15, color='blue',linewidth=1,ls='--',label='Percentile 75')
plt.fill_between(np.arange(0,11), q5.r15, q95.r15,facecolor='red',alpha=0.15)
plt.fill_between(np.arange(0,11), q25.r15, q75.r15,facecolor='blue',alpha=0.15)
plt.xticks(np.arange(0,11))
plt.xlim([0,10])
plt.xlabel('Years')
plt.ylim([-2250,2250])
plt.ylabel('Cummulative deviation respect average surface water supplies (taf)')
plt.legend()
