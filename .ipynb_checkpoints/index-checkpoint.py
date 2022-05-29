# package import statement
import imp
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)

#create object of call
obj=SmartConnect(api_key="2GvelEkX")

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

print(historicalData())
