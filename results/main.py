import pandas as pd

df1 = pd.read_csv('class_gradebook_group_01_recent_score.csv')
df2 = pd.read_csv('class_gradebook_group_02_recent_score.csv')
df3 = pd.read_csv('class_gradebook_group_03_recent_score.csv')
df4 = pd.read_csv('class_gradebook_group_04_recent_score.csv')
df5 = pd.read_csv('class_gradebook_group_05_recent_score.csv')

print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())
print(df5.head())

print(df1.info())
print(df2.info())
print(df3.info())
print(df4.info())
print(df5.info())

print(df1.tail())
print(df2.tail())
print(df3.tail())
print(df4.tail())
print(df5.tail())

print(df1.shape())
print(df2.shape())
print(df3.shape())
print(df4.shape())
print(df5.shape())

print(df1.columns())
print(df2.columns())
print(df3.columns())
print(df4.columns())
print(df5.columns())

print(df1.dtype())
print(df2.dtype())
print(df3.dtype())
print(df4.dtype())
print(df5.dtype())

df1_cleaned = df1.dropna()
df2_cleaned = df2.dropna()
df3_cleaned = df3.dropna()
df4_cleaned = df4.dropna()
df5_cleaned = df5.dropna()