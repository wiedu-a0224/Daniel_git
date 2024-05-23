import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

Client=MongoClient("mongodb://localhost:27017/")
db=Client.IoTDatabase
col=db.IoTDatabase

df=pd.DataFrame(col.find())
Client.close()
# print(df)
#print(df.裝置.value_counts())

fig, ax=plt.subplots( nrows=5, ncols=1, sharex=True,sharey=True,figsize=(8,8))
fig.text(0.5, 0.04, "DateTime", ha="center")
fig.text(0.04, 0.5, "Temperature", va="center",rotation="vertical")
n=0
colors=['r', 'b', 'y', 'g', 'c']
for name in df.裝置.sort_values().unique():
    x=df[df.裝置==name].時間
    y=df[df.裝置==name].溫度
    ax[n].plot(x,y, color=colors[n], label=name)
    ax[n].grid()
    ax[n].legend(loc="upper right")
    n+=1

plt.suptitle("Sensor temperature")
plt.show()
