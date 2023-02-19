import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

''' 
# Load the data
import os 
for dirname, _, filenames in os.walk('data_archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
'''

# Read the data
df = pd.read_csv('data_archive/tips.csv')
# print(df.head())
# print(df.info())
# print(df.describe())
'''
for x in df.columns:
    if df[x].dtypes == 'object':
        print(df[x].unique())

sns.jointplot(x='total_bill', y='tip', data=df, color='green')
sns.jointplot(x='total_bill', y='tip', data=df, ratio=4, height=6)
print(plt.show())
'''

sns.boxplot(x='day', y='total_bill', data=df, palette='husl')
sns.swarmplot(x='day', y='total_bill', data=df, color='black')
print(plt.show())
