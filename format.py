from connexion import connexion
import pandas as pd

con = connexion("localhost", "root", "", "securite")

a = "SELECT * FROM fw"

df = pd.read_sql(a,con)
