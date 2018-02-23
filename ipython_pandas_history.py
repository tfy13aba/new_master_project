# coding: utf-8
import pandas as pd
df = pd.read_csv('file1.txt
df = pd.read_csv('file1.txt', header=None, names=['timestamp','dig','channel','q'])
print df
print (df)
df = pd.read_csv('file1.txt', header=None, sep=' ',names=['timestamp','dig','channel','q'])
print (df)
print (df[df.q < 100])
df = df[df.q > 1000]
print(df)
df[df.q > 1000 && df.timestamp > 5000]
df[df.q > 1000 & df.timestamp > 5000]
df[df.q > 1000 and df.timestamp > 5000]
df[(df.q > 1000) & (df.timestamp > 5000)]
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
plt.hist(df.timestamp)
plt.shop()
plt.show()
plt.hist(df.timestamp)
plt.show(block=False)
plt.hist(df.timestamp)
plt.show(block=False)
plt.show(block=False)
plt.yscale('log')
plt.hist(df.timestamp)
plt.show(block=False)
plt.show(block=False)
df.memory_usage(deep=True).sum()
df.q.sum()
df.to_pickle("pandas_file1.pkl")
get_ipython().magic('save ipython_pandas_history.py')
get_ipython().magic('save ipython_pandas_history.py ~0/')
