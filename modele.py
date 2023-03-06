from connexion import connexion
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter



con = connexion("localhost", "root", "", "securite")

a = "SELECT * FROM fw"

df = pd.read_sql(a,con)

"""
print(df.head())

print(df.info())

print(df.shape)

print(df.action.value_counts())

print(df.isna().sum())
"""

X = df.drop("action", axis=1)
y = df.action 
print(df.iloc[:1,:1])
liste = []
for i in range(df.shape[0]) :
    
    ind = df.iloc[:1,:1]
    liste.append(ind)
    
    
