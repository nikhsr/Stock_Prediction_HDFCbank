#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
import pandas as pd
print("Content-Type:text/html")
print("""""")
print("    <link href='admin/assets/plugins/bootstrap/css/bootstrap.min.css' rel='stylesheet'>")
print("    <link href='admin/main/css/style.css' rel='stylesheet'>")
print("<body><center>")
df = pd.read_csv("G:/Training python/Data/TC1-HDFCBANK.csv")
data1=df['Date']
data2=df['Open Price']
data3=df['High Price']
data4=df['Low Price']
data5=df['Last Traded Price']
data6=df['Close Price']
data7=df['Total Traded Quantity']
data8=df['Turnover (in Lakhs)']
l1=int(len(data1)*0.7)
l2=int(len(data1)-l1)
dd=[data1,data2,data3,data4,data5,data6,data7,data8];
print("<html><h1 align='center'>Test Data</h1><table class='table table-bordered' align='center' style='font-size:12px;'>")
print("<tr><th>Date</th><th>Open Price</th><th>High Price</th><th>Low Price</th><th>Last Traded Price</th><th>Close Price</th><th>Total Traded Quantity</th><th>Turnover (in Lakhs)</th></tr>")
for i in  range(l2):
 print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(dd[0][i],dd[1][i],dd[2][i],dd[3][i],dd[4][i],dd[5][i],dd[6][i],dd[7][i]))
print("</table></html>")
