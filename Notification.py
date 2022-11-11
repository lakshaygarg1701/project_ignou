import time
import email
import smtplib
import imaplib
import mailparser
import sqlite3
from datetime import datetime as dt
import os
from dateutil.parser import parse
import datetime

list1=[]
conn1=sqlite3.connect('mprf/db.sqlite3')
crs1=conn1.cursor()
today=dt.now().date()
crs1.execute('select * from event, event_detail where event_detail.id1=event.id1')
td=datetime.timedelta(days=1)
user="garglakshay631@gmail.com"
password="abcd@1234"
serversmtp = smtplib.SMTP_SSL('smtp.gmail.com')
serversmtp.login(user, password)
print('\nStart',dt.now())
for x in crs1:
    print('\n',x[0],x[1],x[5],x[-2],x[-1])
    print(parse(x[5]).date(),type(parse(x[5]).date()),today,type(today))
    if parse(x[5]).date()==today+td:
        msg="Hi "+x[-1]+"\n"+"You have an upcoming event "+x[1]+" tomorrow"
        print(msg)
        serversmtp.sendmail(user,x[-1],msg)
print('\nClose',dt.now())
conn1.close()