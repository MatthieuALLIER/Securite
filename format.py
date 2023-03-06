import pandas as pd 

#observation du fichier log ayant la plus petite difficulte 
log3 = pd.read_csv("log_fw_3.csv", header=0)

firstlog = pd.read_csv("firstlog.csv", sep=";")
#print(firstlog.head())

firstlog = firstlog.drop(firstlog.iloc[:,7:],axis = 1)

firstlog.columns = ["datetime", "ipsrc", "ipdst","proto","dstport", "action", "policyid"]

print(firstlog.head())


print(firstlog.info())



##########################################################################

from connexion import connexion
import pandas as pd

con = connexion("localhost", "root", "", "securite")

a = "SELECT * FROM fw"

df = pd.read_sql(a,con)

print(df.head())
    

