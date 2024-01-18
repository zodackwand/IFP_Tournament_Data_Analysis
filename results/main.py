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