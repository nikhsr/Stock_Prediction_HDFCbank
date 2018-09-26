#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
from  Project import finalproject as fp
import cgi
l=fp.Project()
request=cgi.FieldStorage()
pred=int(request.getvalue('year'))
inter,slp=l.Slope_Inter_YCP()
pre=l.Prediction_YCP(pred)
result = '{"sl": "'+str(slp)+'", "in": "'+ str(inter) +'", "pr": "'+ str(pre) +'"}';
print("Content-Type:text/html")
print("""""")
print("<html>")
print("<p>{}</p>".format(result))
print("</html>")








