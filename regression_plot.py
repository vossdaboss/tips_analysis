import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data_archive/tips.csv')

# Regression plot
# sns.regplot(x='total_bill', y='tip', data=df)

# Specifiy estimators like mean, median, etc.
'''
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
sns.regplot(x='total_bill', y='tip', data=df, x_estimator=np.mean)

plt.subplot(2, 2, 2)
sns.regplot(x='total_bill', y='tip', data=df, x_estimator=np.median)
print(plt.show())
'''
#Cosmetic parameters like color, size, etc.
plt.figure(figsize=(15, 15))

plt.subplot(3, 3, 1)
sns.regplot(x='total_bill', y='tip', data=df, color='purple')

plt.subplot(3, 3, 2)
sns.regplot(x='total_bill', y='tip', data=df, marker='D') # marker='D' is a diamond

plt.subplot(3, 3, 3)
sns.regplot(x='total_bill', y='tip', data=df, marker='+') # marker='+' is a plus sign

plt.subplot(3, 3, 4)
sns.regplot(x='total_bill', y='tip', data=df, marker='o') # marker='o' is a circle

plt.subplot(3, 3, 5)
sns.regplot(x='total_bill', y='tip', data=df, marker='s') # marker='s' is a square

plt.subplot(3, 3, 6)
sns.regplot(x='total_bill', y='tip', data=df, marker='D', scatter_kws= {'color': 'blue'}, line_kws={'color': 'red', 'linewidth': 3.1}) 
print(plt.show())
