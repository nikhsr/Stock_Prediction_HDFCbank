import math
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
model = LinearRegression()

class Project2:
    def Read1(self):
        df=pd.read_csv("G:/Training python/Data/TC1-HDFCBANK.csv")
        df['Date1']=pd.to_datetime(df['Date'])
        df['Date1']=df['Date1'].map(dt.datetime.toordinal)
        self.Date=df['Date']
        self.Date1=df['Date1']
        self.OpenP=df['Open Price']
        self.HighP=df['High Price']
        self.LowP=df['Low Price']
        self.LastTP=df['Last Traded Price']
        self.CloseP=df['Close Price']
        self.TotalTradeQ=df['Total Traded Quantity']
        self.Turnover=df['Turnover (in Lakhs)']
        return self.Date,self.Date1,self.OpenP,self.HighP,self.LowP,self.LastTP,self.CloseP,self.TotalTradeQ,self.Turnover

    def Residual_Scr_CP(self):
        self.Read1()
        C1=np.array(self.CloseP)
        C2=np.array(self.Turnover)
        C1=C1.reshape(len(C1), 1)
        C2=C2.reshape(len(C2), 1)
        model.fit(C1,C2)
        SS1=model.score(C1, C2)
        RR1=math.sqrt(SS1)
        return RR1,SS1
