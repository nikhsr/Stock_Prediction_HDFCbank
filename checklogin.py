#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
import pymysql
import cgi
print("Content-Type:text/html")
print("""""")
print("<html>")
db=pymysql.connect(host='localhost',user='root',password='admin',db='login')
cmd=db.cursor()
request=cgi.FieldStorage()
email=request.getvalue('email')
pwdd=request.getvalue('pwdd')
q="select * from checklogin where emailid='{0}' AND password='{1}'".format(email,pwdd)
cmd.execute(q)
row=cmd.fetchall()
if(len(row)==0):
    print("<h2 align='center'>Register Yourself</h2>")
    print("<span  align='center'>If Already Registered Then Check Your Password</span><br>")
else:
    print('<meta HTTP-EQUIV="REFRESH" content="0; url=http://localhost/HDFCML/Project/Home.py">')
print("</html>")
