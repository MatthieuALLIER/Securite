from connexion import connexion
import pandas as pd

con = connexion("localhost", "root", "", "securite")

a = "SELECT * FROM fw"

df = pd.read_sql(a,con)

print(df.head())


print(df.info())

print(df.shape)

print(df.action.value_counts())

print(df.isna().sum())