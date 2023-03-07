from connexion import connexion
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
import sqlalchemy

#load data
con = connexion("localhost", "root", "", "securite")
a = "SELECT * FROM fw"
df = pd.read_sql(a,con)

#Add freq on this port
freqSamePort = df.groupby(["ipsrc", "dstport"]).size().reset_index()
freqSamePort.columns = ["ipsrc", "dstport", "sameport"]

#add freq on different port
freqDiffPort = freqSamePort["ipsrc"].value_counts().reset_index()
freqDiffPort.columns = ["ipsrc", "diffport"]

df = df.merge(freqSamePort, on = ["ipsrc", "dstport"])
df = df.merge(freqDiffPort, on = "ipsrc")

dfFormat = df.copy()
dfFormat["datetime"] = pd.to_datetime(df['datetime'])
dfFormat["datetime"] = dfFormat["datetime"] - min(dfFormat["datetime"])
dfFormat["datetime"] = dfFormat["datetime"].astype('int64')/ 10**9
dfFormat["action"] = np.where(dfFormat["action"] == "DENY", 1, 0)
dfFormat = dfFormat.drop(["ipsrc","ipdst","proto"], axis=1)
dfFormat = dfFormat.replace("", 0)

#load model
findBrut = IsolationForest().fit(dfFormat.drop("diffport", axis=1))
findScan = IsolationForest().fit(dfFormat.drop("sameport", axis=1))

#predict
isBrut = findBrut.predict(dfFormat.drop("diffport", axis = 1))
isScan = findScan.predict(dfFormat.drop("sameport", axis = 1))

pred = ((isBrut == 1) | (isScan == 1)).astype(int)

pd.Series(pred).value_counts()

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/securite")

pd.Series(pred).to_sql("result", engine, if_exists="replace")














