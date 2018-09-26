#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
import pymysql
import cgi
print("Content-Type: text/html")
print("""""")
print("<html>")
db=pymysql.connect(host='localhost',user='root',password='admin',db='login')
cmd=db.cursor()
request=cgi.FieldStorage()
fname=request.getvalue('fname')
lname=request.getvalue('lname')
uid=request.getvalue('uid')
eid=request.getvalue('eid')
d=request.getvalue('d')
pwd=request.getvalue('pwd')
cpwd=request.getvalue('cpwd')
if(pwd==cpwd):
    q="insert into checklogin values('{0}','{1}','{2}','{3}','{4}','{5}')".format(fname, lname, uid, eid,d,pwd)
    cmd.execute(q)
    db.commit()
    db.close()
    print('<meta HTTP-EQUIV="REFRESH" content="0; url=http://localhost/HDFCML/Project/Home.py">')
else:
    print("<h2 align='center'>Password Don't Match</h2>")
    print("<span><a href=Registration.py align='center'>Try Again</a></span><br>")
print("</html>")