# def isScan(df):
#     nextdate = past.datetime[1:].reset_index(drop=True)
#     diffdate = nextdate - past.datetime[:-1].reset_index(drop=True)
#     diffdate = diffdate.dt.total_seconds()    
#     maxReq3sec = 

# def isBrutForce(df):
#     pass

# attaque = []
# for i in range(df.shape[0]):    
#     ind = df.iloc[i,1]
#     past = df.iloc[0:i+1,:]    
#     past = past[past["ipsrc"] == ind]    
#     scan = 0
#     brutForce = 0    
#     if past.shape[0] > 1:
#         scan = isScan(past)
#         brutForce = isBrutForce(past)    
#     if scan == 1 or brutForce == 1:
#         category = 1
#     else:
#         category = 0        
#     attaque.append(category)

from connexion import connexion
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

chunk = pd.read_csv('log_fw_4.csv',chunksize=1000000, delimiter=";",header=None)
df = pd.concat(chunk)
df = df[[0,1,2,3,5,6,7]]
df.columns = ["datetime","ipsrc","ipdst","proto","dstport","policyid","action"]

freqSamePort = df.groupby(["ipsrc", "dstport"]).size().reset_index()
freqSamePort.columns = ["ipsrc", "dstport", "sameport"]

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

train, test = train_test_split(dfFormat, train_size=200000, test_size=100000)

clf = IsolationForest().fit(train)
pred = clf.predict(train)

fig = px.scatter(x=Xpca[:,0], y=Xpca[:,1], color=pred)
fig.show()



















