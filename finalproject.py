import pandas as pd
import datetime as dt
import LinearRegression as lr
import MultipleRegression as mr
l=lr.LinearRegression()
m=mr.MultipleRegression()

class Project:
    def Read(self):
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

    def Year_Month_Day(self):
        R=self.Read()
        self.Date2=R[0]
        df=pd.read_csv("G:/Training python/Data/TC1-HDFCBANK.csv")
        df['year']=pd.DatetimeIndex(df['Date']).year
        self.yr=df['year'].astype(int)
        self.Year=set(self.yr)
        self.Year=list(self.Year)
        self.Year.sort(reverse=True)

        #Month
        df['month']=pd.DatetimeIndex(df['Date']).month
        self.mn=df['month'].astype(int)
        self.Month=set(self.mn)
        self.Month=list(self.Month)
        self.Month.sort()

        self.month=list()
        self.day=list()
        self.year=list()
        while (True):
            for i in self.Date2:
                mon, da, yr=str(i).split('/')
                self.month.append(int(mon.strip()))
                self.day.append(da)
                self.year.append(int(yr.strip()))
            return self.Year,self.Month,self.month, self.day, self.year

    def Y_CP(self):
        R=self.Read()
        self.ClosePrice=R[6]
        self.Year_Month_Day()
        self.year.sort(reverse=True)
        self.D_CP=dict()
        self.D_CP_M=dict()
        for J in self.Year:
            self.Y=J
            self.CP=list()
            self.k=0
            for i in self.ClosePrice:
                # print(year[k], Y, i)
                if (self.year[self.k] == self.Y):
                    self.CP.append(i)
                self.k=self.k + 1
            self.D_CP.setdefault(self.Y, self.CP)
            self.D_CP_M.setdefault(self.Y, l.mean(self.CP))
        #print(self.D_CP_M)
        #print(self.D_CP.get(2011, 'not'))
        return self.D_CP_M

    def Y_TurnOver(self):
        R=self.Read()
        self.turnover=R[8]
        self.Year_Month_Day()
        self.year.sort(reverse=True)
        self.D_turn=dict()
        for J in self.Year:
            self.Y=J
            self.Turn=list()
            self.k1=0
            for j in self.turnover:
                if (self.year[self.k1] == self.Y):
                    self.Turn.append(j)
                self.k1=self.k1 + 1
            self.D_turn.setdefault(self.Y,l.mean(self.Turn))
        return self.D_turn

    def Y_OPenP(self):
        R=self.Read()
        self.OpenPrice=R[2]
        self.Year_Month_Day()
        self.year.sort(reverse=True)
        self.month.sort()
        self.D_OP=dict()
        for J in self.Year:
            self.Y=J
            self.Open=list()
            self.k2=0
            for j in self.OpenPrice:
                if (self.year[self.k2] == self.Y):
                    self.Open.append(j)
                self.k2=self.k2 + 1
            self.D_OP.setdefault(self.Y,l.mean(self.Open))
        return self.D_OP

    def Y_TT(self):
        R=self.Read()
        self.TotalT=R[7]
        self.Year_Month_Day()
        self.year.sort(reverse=True)
        self.month.sort()
        self.D_TT=dict()
        for J in self.Year:
            self.Y=J
            self.TT=list()
            self.k3=0
            for j in self.TotalT:
                if (self.year[self.k3] == self.Y):
                    self.TT.append(j)
                self.k3=self.k3 + 1
            self.D_TT.setdefault(self.Y,l.mean(self.TT))
        return self.D_TT

    def M_CP(self):
        R=self.Read()
        self.Date2=R[0]
        self.ClosePrice=R[6]
        self.Year_Month_Day()
        self.D_MCP=dict()
        for J in self.Year:
            self.MCP=dict()
            for K in range(1, 13):
                self.q=0
                self.L1=list()
                for K1 in self.Date2:
                    if (str(K1).startswith(str(K)) and str(K1).endswith(str(J))):
                        self.L1.append(self.ClosePrice[self.q])
                        self.MCP.setdefault(K, l.mean(self.L1))
                        # print( J,K,q,CloseP[q])
                    self.q=self.q + 1
                    self.D_MCP.setdefault(J, self.MCP)
        K1=self.D_MCP.get(2016, 'not')
        YY=2016
        for i in range(6, 13):
            K1.setdefault(i, 0)
        self.D_MCP.update({YY: K1})
        return self.D_MCP

    def M_TurnOver(self):
        R=self.Read()
        self.Date2=R[0]
        self.turnover=R[8]
        self.Year_Month_Day()
        self.D_MT=dict()
        for J in self.Year:
            self.MT=dict()
            for K in range(1, 13):
                self.q1=0
                self.L2=list()
                for K1 in self.Date2:
                    if (str(K1).startswith(str(K)) and str(K1).endswith(str(J))):
                        self.L2.append(self.turnover[self.q1])
                        self.MT.setdefault(K,l.mean(self.L2))
                    self.q1=self.q1 + 1
                    self.D_MT.setdefault(J, self.MT)
        K2=self.D_MT.get(2016, 'not')
        YY=2016
        for i in range(6, 13):
            K2.setdefault(i, 0)
        self.D_MT.update({YY: K2})
        return self.D_MT

    def M_OP(self):
        R=self.Read()
        self.Date2=R[0]
        self.OP=R[2]
        self.Year_Month_Day()
        self.D_MOP=dict()
        for J in self.Year:
            self.MOP=dict()
            for K in range(1, 13):
                self.q2=0
                self.L3=list()
                for K1 in self.Date2:
                    if (str(K1).startswith(str(K)) and str(K1).endswith(str(J))):
                        self.L3.append(self.OP[self.q2])
                        self.MOP.setdefault(K,l.mean(self.L3))
                    self.q2=self.q2+ 1
                    self.D_MOP.setdefault(J, self.MOP)
        K3=self.D_MOP.get(2016, 'not')
        YY=2016
        for i in range(6, 13):
            K3.setdefault(i, 0)
        self.D_MOP.update({YY: K3})
        return self.D_MOP

    def M_TT(self):
        R=self.Read()
        self.Date2=R[0]
        self.TT=R[7]
        self.Year_Month_Day()
        self.D_MTT=dict()
        for J in self.Year:
            self.MTT=dict()
            for K in range(1, 13):
                self.q3=0
                self.L4=list()
                for K1 in self.Date2:
                    if (str(K1).startswith(str(K)) and str(K1).endswith(str(J))):
                        self.L4.append(self.TT[self.q3])
                        self.MTT.setdefault(K,l.mean(self.L4))
                    self.q3=self.q3+ 1
                    self.D_MTT.setdefault(J, self.MTT)
        K4=self.D_MTT.get(2016, 'not')
        YY=2016
        for i in range(6, 13):
            K4.setdefault(i, 0)
        self.D_MTT.update({YY: K4})
        return self.D_MTT

    def Slope_Inter_YCP(self):
        self.D=self.Y_CP()
        self.year1=self.D.keys()
        self.Mean1=self.D.values()
        self.inter1=l.intercept(self.Mean1, self.year1)
        self.slp1=l.slope(self.Mean1,self. year1)
        return self.inter1,self.slp1

    def Prediction_YCP(self,pred):
        self.D=self.Y_CP()
        self.year1=self.D.keys()
        self.Mean1=self.D.values()
        self.predict1=l.predict(self.Mean1,self.year1,pred)
        return self.predict1

    def Slope_Inter_YTurn(self):
        self.D1=self.Y_TurnOver()
        self.year2=self.D1.keys()
        self.Mean2=self.D1.values()
        self.inter2=l.intercept(self.Mean2, self.year2)
        self.slp2=l.slope(self.Mean2, self.year2)
        return self.inter2, self.slp2

    def Prediction_YTurn(self,pred):
        self.D1=self.Y_TurnOver()
        self.year2=self.D1.keys()
        self.Mean2=self.D1.values()
        self.predict2=l.predict(self.Mean2, self.year2, pred)
        return self.predict2

    def Slope_Inter_YOP(self):
        self.D3=self.Y_OPenP()
        self.year3=self.D3.keys()
        self.Mean3=self.D3.values()
        self.inter3=l.intercept(self.Mean3, self.year3)
        self.slp3=l.slope(self.Mean3, self.year3)
        return self.inter3, self.slp3

    def Prediction_YOP(self,pred):
        self.D3=self.Y_TurnOver()
        self.year3=self.D3.keys()
        self.Mean3=self.D3.values()
        self.predict3=l.predict(self.Mean3, self.year3, pred)
        return self.predict3

    def Slope_Inter_YTT(self):
        self.D4=self.Y_TT()
        self.year4=self.D4.keys()
        self.Mean4=self.D4.values()
        self.inter4=l.intercept(self.Mean4, self.year4)
        self.slp4=l.slope(self.Mean4, self.year4)
        return self.inter4, self.slp4

    def Prediction_YTT(self,pred):
        self.D4=self.Y_TT()
        self.year4=self.D4.keys()
        self.Mean4=self.D4.values()
        self.predict4=l.predict(self.Mean4, self.year4, pred)
        return self.predict4


    def Prediction_CP_Turnover(self,CP):
        self.Read()
        self.pre1=l.predict(self.CloseP,self.Turnover,CP)
        return self.pre1

    def Prediction_TotalTrade_Turnover(self,TT):
        self.Read()
        self.pre2=l.predict(self.TotalTradeQ,self.Turnover,TT)
        return self.pre2

    def Prediction_CP_TT_Turn(self,CP,TT):
        self.Read()
        self.pre3=m.predict(self.Turnover,self.CloseP,self.TotalTradeQ,CP,TT)
        return self.pre3

    def Intercept_Slope_CP_Turn(self):
        self.Read()
        I1=l.intercept(self.CloseP,self.Turnover)
        S1=l.slope(self.CloseP,self.Turnover)
        return I1,S1

    def Intercept_Slope_TT_Turn(self):
        self.Read()
        I2=l.intercept(self.TotalTradeQ, self.Turnover)
        S2=l.slope(self.TotalTradeQ, self.Turnover)
        return I2,S2

    def Intercept_Slope_CP_TT_Turn(self):
        self.Read()
        I3=m.intercept(self.Turnover,self.CloseP,self.TotalTradeQ)
        S3=m.slope(self.Turnover,self.CloseP,self.TotalTradeQ)
        return I3,S3


    def Prediction_MCP(self,M,Y):
        Z=self.Year_Month_Day()
        YY=Z[0]
        YY.sort()
        DCP=self.M_CP()
        MY1=list()
        try:
            for d in DCP.values():
                for y in YY:
                    MY1.append(DCP[y][M])
                break
            self.PP=l.predict(YY,MY1,Y)
            I4=l.intercept(YY,MY1)
            S4=l.slope(YY,MY1)
            return self.PP,I4,S4
        except KeyError as k:
            pass


    def Prediction_MTurnover(self,M,Y):
        Z=self.Year_Month_Day()
        YY=Z[0]
        YY.sort()
        Dturn=self.M_TurnOver()
        MY2=list()
        try:
            for d in Dturn.values():
                for y in YY:
                    MY2.append(Dturn[y][M])
                break
            self.PP2=l.predict(YY,MY2,Y)
            I5=l.intercept(YY,MY2)
            S5=l.slope(YY,MY2)
            return self.PP2,I5,S5
        except KeyError as k:
            pass

    def Prediction_MOP(self,M,Y):
        Z=self.Year_Month_Day()
        YY=Z[0]
        YY.sort()
        DOP=self.M_OP()
        MY3=list()
        try:
            for d in DOP.values():
                for y in YY:
                    MY3.append(DOP[y][M])
                break
            self.PP3=l.predict(YY,MY3,Y)
            I6=l.intercept(YY,MY3)
            S6=l.slope(YY,MY3)
            return self.PP3,I6,S6
        except KeyError as k:
            pass

    def Prediction_MTT(self,M,Y):
        Z=self.Year_Month_Day()
        YY=Z[0]
        YY.sort()
        DTT=self.M_TT()
        MY4=list()
        try:
            for d in DTT.values():
                for y in YY:
                    MY4.append(DTT[y][M])
                break
            self.PP4=l.predict(YY,MY4,Y)
            I7=l.intercept(YY,MY4)
            S7=l.slope(YY,MY4)
            return self.PP4,I7,S7
        except KeyError as k:
            pass

