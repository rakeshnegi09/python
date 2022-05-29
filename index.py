# package import statement
import imp
from tkinter.tix import COLUMN
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)

#create object of call
obj=SmartConnect(api_key="2GvelEkX")

#2GvelEkX 
#KnBVAfX5 

#login api call

data = obj.generateSession("R809759","Lovesuck0909")
refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)
import json
import pandas as pd
from datetime import datetime


def historicalData ():
    try:
        historicalParams = {
            "exchange":"NSE",
            "symboltoken":"3045",
            "interval":"ONE_MINUTE",
            "fromdate": "2021-02-10 09:15",
             "todate": "2021-02-20 09:16"
        }

        return obj.getCandleData(historicalParams)
    except Exception as e:
        print(e)

res = historicalData()
columns = ['timestamp',"O","C","L","H","V"]

df = pd.DataFrame(res['data'],columns=columns)
df['timestamp'] = pd.to_datetime(df['timestamp'],format='%Y-%m-%dT%H:%M:%S')
df= df.round(decimals=2)
df






