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
summary('Vulnerability','Vulnerability Category',2016)
data.loc[1292,'WRI Category'] = 'Medium'
data.loc[1193,'Vulnerability Category'] = 'Very Low'
data.loc[1202,'Vulnerability Category'] = 'Very Low'
data.loc[1205,'Vulnerability Category'] = 'Very Low'
data.loc[1858,'Vulnerability Category'] = 'Very Low'
data.loc[1858,' Lack of Adaptive Capacities']=np.mean(data[' Lack of Adaptive Capacities'])
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
fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(24, 12))
plt.subplots_adjust(left=0.2, bottom=0, right=1, top=1, wspace=0, hspace=0.5)
for ax,i in zip(axs.ravel(),years):
    ax.bar(bottom10(i)['Region'],bottom10(i)['WRI'],)
    ax.set_title(i)
    ax.tick_params(labelrotation=90)
    ax.set_ylim([0,3])
    sns.despine()
plt.show()
data.describe()
ys = ['WRI','Exposure','Vulnerability','Susceptibility','Lack of Coping Capabilities',' Lack of Adaptive Capacities']
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 12))
for ax,i in zip(axs.ravel(),ys):
    az.plot_kde(data[i],fill_kwargs={"alpha":0.5},ax=ax)
    ax.set_title(i)
    sns.despine()
plt.show()
import warnings
warnings.filterwarnings("ignore")
ys = ['WRI','Exposure','Vulnerability','Susceptibility','Lack of Coping Capabilities',' Lack of Adaptive Capacities']
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 12))
for ax,i in zip(axs.ravel(),ys):
    sns.boxplot(data[i],ax=ax)
    ax.set_title(i)
    sns.despine()
plt.show()
sns.heatmap(data.corr(), annot=True,linewidths=.5)
sns.pairplot(data=data)

plt.show()
ys = ['WRI','Exposure','Vulnerability','Susceptibility']
fig, ((a,b),(c,d)) = plt.subplots (2, 2, figsize=(12, 12))
for i,t in zip(ys,[a,b,c,d]):
    sns.boxplot(x=i+' Category', y=i,data=data.sort_values(by=i), ax = t)
    t.legend(ncol=3)
    t.set_title(i)
sns.despine()
ys = ['WRI','Exposure','Vulnerability','Susceptibility']
fig, ((a,b),(c,d)) = plt.subplots (2, 2, figsize=(12, 12))
for i,t in zip(ys,[a,b,c,d]):
    sns.violinplot(x=i+' Category', y=i,data=data.sort_values(by=i), ax = t)
    t.legend(ncol=3)
    t.set_title(i)
sns.despine()
col = ['WRI','Exposure','Vulnerability','Susceptibility','Lack of Coping Capabilities',' Lack of Adaptive Capacities']
col_hue = ['WRI Category','Exposure Category','Vulnerability Category','Susceptibility Category',None,None]
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(20, 9))
plt.subplots_adjust(hspace=0.5)
for ax,i,j in zip(axs.ravel(),col,col_hue):
    sns.lineplot(data=data.sort_values(by='Year'), x="Year", y=i, hue=j,markers=True,dashes=True,ci='sd',ax=ax)
    ax.set_title(i)
    ax.tick_params(labelrotation=90)
    sns.despine()
    if(i!='WRI'):
        ax.legend().set_visible(False)
    else:
        ax.legend(ncol=3)
sns.despine()
ys = ['WRI','Exposure','Vulnerability','Susceptibility']
fig, ((a,b),(c,d)) = plt.subplots (2, 2, figsize=(16, 12))
for i,t in zip(ys,[a,b,c,d]):
    sns.swarmplot(x='Year', y=i, hue=i+' Category',data=data.sort_values(by='Year'), ax = t)
    if(i=='WRI'):
        t.legend(ncol=3)
    else:
        t.legend().set_visible(False)
    t.set_title(i)
sns.despine()

