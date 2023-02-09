import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import arviz as az
import warnings
warnings.filterwarnings("ignore")
data =  pd.read_csv("../input/global-disaster-risk-index-time-series-dataset/world_risk_index.csv")
data.head()
len(data['Year'].unique()),np.sort(data['Year'].unique()),len(data['Region'].unique())
data.isna().sum().sum()
def summary(col1,col2,year):
    pivot = pd.pivot_table(data, values=[col1], index=['Year',col2],
                    aggfunc={col1: [min, max, np.mean,np.std]})
    pivot = pivot.sort_values(by=(col1,'mean')).reindex(np.sort(data['Year'].unique()), level=0)

    return pivot.loc[year,:]
def pivot(col1,col2):
    pivot = pd.pivot_table(data, values=[col1], index=[col2,'Year'],
                    aggfunc={col1: [min, max, np.mean,np.std]})
    pivot = pivot.sort_values(by=(col1,'mean')).reindex(np.sort(data['Year'].unique()), level=1)
    pivot = pivot.reset_index()
    return pivot
data.isna().sum().sum()
data[pd.isnull(data).any(axis=1)]
summary('WRI','WRI Category',2020)
summary('Vulnerability','Vulnerability Category',2019)
#patch-2
summary('Vulnerability','Vulnerability Category',2016)
data['Year']= data['Year'].astype('str')
def top10(year):
    return data[data['Year']==year].sort_values(by='WRI')[::-1].head(10)
def bottom10(year):
    return data[data['Year']==year].sort_values(by='WRI').head(10)
    years= np.sort(data['Year'].unique())[::-1]
    fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(24, 12))
    plt.subplots_adjust(left=0.2, bottom=0, right=1, top=1, wspace=0, hspace=0.5)

    for ax,i in zip(axs.ravel(),years):
    ax.bar(top10(i)['Region'],top10(i)['WRI'],)
    ax.set_title(i)
    ax.tick_params(labelrotation=90)
    ax.set_ylim([0,55])
    sns.despine()

plt.show()
   
data.describe()
