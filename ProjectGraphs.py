import  matplotlib.pyplot as plt
import seaborn as sns
import LinearRegression as lr
import MultipleRegression as mr
import pandas as pd
from pandas import DataFrame
import datetime as dt
import numpy as np
import finalproject as fp
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
l=lr.LinearRegression()
m=mr.MultipleRegression()
model = LinearRegression()
f=fp.Project()

df=pd.read_csv("G:/Training python/Data/TC1-HDFCBANK.csv")
df['Date1']=pd.to_datetime(df['Date'])
df['Date1']=df['Date1'].map(dt.datetime.toordinal)
Date=df['Date']
Date1=df['Date1']
OpenP=df['Open Price']
HighP=df['High Price']
LowP=df['Low Price']
LastTP=df['Last Traded Price']
CloseP=df['Close Price']
TotalTradeQ=df['Total Traded Quantity']
Turnover=df['Turnover (in Lakhs)']

CP_train,CP_test=train_test_split(CloseP,test_size=0.3)
TTQ_train,TTQ_test=train_test_split(TotalTradeQ,test_size=0.3)
OP_train,OP_test=train_test_split(OpenP,test_size=0.3)
Turn_train,Turn_test=train_test_split(Turnover,test_size=0.3)


'''plt.scatter(CP_train,Turn_train, color='blue')
plt.plot(CP_train, l.predict1(CP_train,Turn_train), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on  Trained Data(Close Price VS TurnOver(in Lakhs))')
plt.xlabel('Close Price')
plt.ylabel('Turnover(in Lakhs)')
plt.show()
plt.scatter(CP_test,Turn_test, color='blue')
plt.plot(CP_test, l.predict1(CP_test,Turn_test), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on Test Data(Close Price VS TurnOver(in Lakhs))')
plt.xlabel('Close Price')
plt.ylabel('Turnover(in Lakhs)')
#plt.xticks(CP_test)
#plt.yticks(Turn_test)
plt.show()

sns.lmplot(x='Close Price',y='Turnover (in Lakhs)',data=df)
plt.title('Prediction Of Turnover On The Basis Of Close Price')
plt.show()
sns.residplot(x='Close Price',y='Turnover (in Lakhs)',data=df)
plt.title('Prediction Of Turnover On The Basis Of Close Price')
plt.show()
sns.factorplot(x='Close Price',y='Turnover (in Lakhs)',data=df,kind='point')
plt.title('Prediction Of Turnover On The Basis Of Close Price')
plt.show()
sns.regplot(x='Close Price',y='Turnover (in Lakhs)',data=df)
plt.title('Prediction Of Turnover On The Basis Of Close Price')
plt.show()
sns.jointplot('Close Price','Turnover (in Lakhs)', data=df,size=5, ratio=3, color="g")
plt.title('Prediction Of Turnover On The Basis Of Close Price')
plt.show()
#residuals
CP_tr=np.array(CP_train)
CP_te=np.array(CP_test)
Turn_tr=np.array(Turn_train)
Turn_te=np.array(Turn_test)
CP_tr=CP_tr.reshape(len(CP_tr),1)
CP_te=CP_te.reshape(len(CP_te),1)
Turn_tr=Turn_tr.reshape(len(Turn_tr),1)
Turn_te=Turn_te.reshape(len(Turn_te),1)
model.fit(CP_tr,Turn_tr)
model.fit(CP_te, Turn_te)
plt.scatter(model.predict(CP_tr), model.predict(CP_tr)-Turn_tr, c='b', s=40,alpha=0.5)
plt.scatter(model.predict(CP_te), model.predict(CP_te)-Turn_te, c='g', s=40)
plt.hlines(y=0,xmin=0,xmax=50)
plt.title('Residuals Plot Trained Close Price Vs Turnover(blue) vs Trained Close Price VS Turnover(green)')
plt.ylabel('Turnover(in Lakhs)')
plt.xlabel('Close Price')
#plt.xticks(x)
#plt.yticks(y)
plt.show()


plt.scatter(TTQ_train,Turn_train, color='blue')
plt.plot(TTQ_train, l.predict1(TTQ_train,Turn_train), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on Trained Data(Total Traded Quantity VS TurnOver(in Lakhs))')
plt.xlabel('Total Traded Quantity')
plt.ylabel('Turnover(in Lakhs)')
plt.show()

plt.scatter(TTQ_test,Turn_test, color='blue')
plt.plot(TTQ_test, l.predict1(TTQ_test,Turn_test), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on Test Data(Total Traded Quantity VS TurnOver(in Lakhs))')
plt.xlabel('Total Traded Quantity')
plt.ylabel('Turnover(in Lakhs)')
plt.show()

sns.residplot(x='Total Traded Quantity',y='Turnover (in Lakhs)',data=df)
plt.title('Prediction Of Turnover On The Basis Of Total Traded Quantity')
plt.show()
sns.factorplot(x='Total Traded Quantity',y='Turnover (in Lakhs)',data=df,kind='point')
plt.title('Prediction Of Turnover On The Basis Of Total Traded Quantity')
plt.show()
sns.regplot(x='Total Traded Quantity',y='Turnover (in Lakhs)',data=df)
plt.title('Prediction Of Turnover On The Basis Of Total Traded Quantity')
plt.show()
sns.jointplot('Total Traded Quantity','Turnover (in Lakhs)', data=df,size=5, ratio=3, color="r")
plt.title('Prediction Of Turnover On The Basis Of Total Traded Quantity')
plt.show()
#residuals
TTQ_tr=np.array(TTQ_train)
TTQ_te=np.array(TTQ_test)
Turn_tr=np.array(Turn_train)
Turn_te=np.array(Turn_test)
TTQ_tr=TTQ_tr.reshape(len(TTQ_tr),1)
TTQ_te=TTQ_te.reshape(len(TTQ_te),1)
Turn_tr=Turn_tr.reshape(len(Turn_tr),1)
Turn_te=Turn_te.reshape(len(Turn_te),1)
model.fit(TTQ_tr,Turn_tr)
model.fit(TTQ_te, Turn_te)
plt.scatter(model.predict(TTQ_tr), model.predict(TTQ_tr)-Turn_tr, c='b', s=40,alpha=0.5)
plt.scatter(model.predict(TTQ_te), model.predict(TTQ_te)-Turn_te, c='g', s=40)
plt.hlines(y=0,xmin=0,xmax=50)
plt.title('Residuals Plot Trained Total Trade Quantity Vs Predicted Turnover(blue) vs Trained Total Trade Quantity VS Predicted Turnover(green)')
plt.ylabel('Turnover(in Lakhs)')
plt.xlabel('Total Trade Quantity')
#plt.xticks(x)
#plt.yticks(y)
plt.show()

plt.scatter(OP_train,Turn_train, color='blue')
plt.plot(OP_train, l.predict1(OP_train,Turn_train), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on Trained Data(Open Price VS TurnOver(in Lakhs))')
plt.xlabel('Open Price')
plt.ylabel('Turnover(in Lakhs)')
plt.show()

plt.scatter(OP_test,Turn_test, color='blue')
plt.plot(OP_test, l.predict1(OP_test,Turn_test), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on Test Data(Open Price VS TurnOver(in Lakhs))')
plt.xlabel('Open Price')
plt.ylabel('Turnover(in Lakhs)')
plt.show()


X = df[['Close Price','Total Traded Quantity']].astype(float) # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Turnover (in Lakhs)'].astype(float)

model.fit(X, Y)
#plt.scatter(X,Y, color='blue')
plt.plot(X, model.predict(X), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction on Test Data(Close Price And Total Traded Quantity VS TurnOver(in Lakhs))')
plt.xlabel('Close Price And Total Traded Quantity')
plt.ylabel('Turnover(in Lakhs)')
plt.show()


DYCP=f.Y_CP()
key=list()
val=list()
for k,v in DYCP.items():
    key.append(k)
    val.append(v)
plt.scatter(key,val, color='blue')
plt.plot(key, l.predict1(key,val), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction Of Average Close Price On The Basis Of Year')
plt.xlabel('Year')
plt.ylabel('Average Close Price')
plt.show()
F1= {'Year': key,'Average Close Price': val}
df1 = DataFrame(F1,columns=['Year','Average Close Price'])
sns.residplot(x='Year',y='Average Close Price',data=df1)
plt.title('Prediction Of Average Close Price On The Basis Of Year')
plt.show()
sns.factorplot(x='Year',y='Average Close Price',data=df1,kind='point')
plt.title('Prediction Of Average Close Price On The Basis Of Year')
plt.show()

DYTurn=f.Y_TurnOver()
key1=list()
val1=list()
for k,v in DYTurn.items():
    key1.append(k)
    val1.append(v)
F2= {'Year': key1,'Average Turnover(in Lakhs': val1}
df2 = DataFrame(F2,columns=['Year','Average Turnover(in Lakhs'])
sns.residplot(x='Year',y='Average Turnover(in Lakhs',data=df2)
plt.title('Prediction Of Average Turnover On The Basis Of Year')
plt.show()
sns.factorplot(x='Year',y='Average Turnover(in Lakhs',data=df2,kind='point')
plt.title('Prediction Of Average Turnover On The Basis Of Year')
plt.show()
plt.scatter(key1,val1, color='blue')
plt.plot(key1, l.predict1(key1,val1), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction Of Average Turnover On The Basis Of Year')
plt.xlabel('Year')
plt.ylabel('Average Turnover(in Lakhs)')
plt.show()

DYTT=f.Y_TT()
key2=list()
val2=list()
for k,v in DYTT.items():
    key2.append(k)
    val2.append(v)
F3= {'Year': key2,'Average Total Traded Quantity': val2}
df3 = DataFrame(F3,columns=['Year','Average Total Traded Quantity'])
sns.residplot(x='Year',y='Average Total Traded Quantity',data=df3)
plt.title('Prediction Of Average Total Traded Quantity On The Basis Of Year')
plt.show()
sns.factorplot(x='Year',y='Average Total Traded Quantity',data=df3,kind='point')
plt.title('Prediction Of Average Total Traded Quantity On The Basis Of Year')
plt.show()
plt.scatter(key2,val2, color='blue')
plt.plot(key2, l.predict1(key2,val2), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction Of Average Total Traded Quantity On The Basis Of Year')
plt.xlabel('Year')
plt.ylabel('Average Total Traded Quantity')
plt.show()

DYOP=f.Y_OPenP()
key3=list()
val3=list()
for k,v in DYOP.items():
    key3.append(k)
    val3.append(v)
F4= {'Year': key3,'Average Open Price': val3}
df4 = DataFrame(F4,columns=['Year','Average Open Price'])
sns.residplot(x='Year',y='Average Open Price',data=df4)
plt.title('Prediction Of Average Open Price On The Basis Of Year')
plt.show()
sns.factorplot(x='Year',y='Average Open Price',data=df4,kind='point')
plt.title('Prediction Of Average Open Price On The Basis Of Year')
plt.show()
plt.scatter(key3,val3, color='blue')
plt.plot(key3, l.predict1(key3,val3), color='red',linewidth=3)
plt.title('Scatter Plot of Prediction Of Average Open Price On The Basis Of Year')
plt.xlabel('Year')
plt.ylabel('Average Open Price')
plt.show()'''


