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

def read_email_from_gmail():
    try:
        conn=sqlite3.connect('db.sqlite3')
        crs=conn.cursor()
        user='garglakshay631@gmail.com'
        password="abcd@1234"
        serverimap = imaplib.IMAP4_SSL('imap.gmail.com')
        serverimap.login(user,password)
        serverimap.select('inbox')
        serversmtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        serversmtp.login(user, password)

        typ, data = serverimap.search(None, 'UnSeen')
        print('\n')
        print('Start',dt.now(),'\n')
        print("Connection",typ)
        print(data)
        mail_ids = data[0]
        
        id_list = mail_ids.split()
        if len(id_list)==0:
            print('Database is up to date')
            print('\nClose',dt.now())
            return
        first_email = int(id_list[0])
        latest_email = int(id_list[-1])
        for i in range(latest_email,first_email-1,-1):
            typ, data = serverimap.fetch(str(i), '(RFC822)' )
            for response_part in data:
                if isinstance(response_part, tuple):
                    mail = mailparser.parse_from_string(str(response_part[-1],'utf-8'))
                    print(mail)
                    name=mail.subject
                    name1=name.split('_')[0]
                    to=mail.to[-1][-1]
                    from_=mail.from_[-1][-1]
                    att=mail.attachments
                    body=mail.text_plain[-1]
                    b=body.split('\r\n')
                    contact=b[-1]
                    date=b[-3]
                    date=dt.strptime(date,'%d %B %Y, %I %p')
                    venue=b[-5]
                    reg=b[-7]
                    dept=b[-9]
                    cat=name.split('_')[-1]
                    if cat=='E-Sport':
                        cat='E-Sports'
                    str1="\r\n".join(b[:-9])
                    filePath=""
                    emailbody=data[0][1]
                    att=email.message_from_bytes(emailbody)
                    for part in att.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue
                        fileName = part.get_filename()

                        if bool(fileName):
                            filePath = os.path.join(os.getcwd(), fileName)
                            if not os.path.isfile(filePath) :
                                print (fileName)
                                fp = open(filePath, 'wb')
                                print(filePath)
                                fp.write(part.get_payload(decode=True))
                                fp.close()
                    crs.execute('insert into event values(null,?,?,?,?,?,?,?,?,?,?,?,?)',(name1,from_,to,str1,date,venue,reg,contact,cat,dept,filePath,dt.now().replace(microsecond=0)))
                    serversmtp.sendmail(to,from_,'Thanks')
        print('\nClose',dt.now())
        conn.commit()
        conn.close()

    except (Exception, e):
        print (str(e))

def notification():
    try:
        list1=[]
        conn1=sqlite3.connect('db.sqlite3')
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

    except Exception as e:
        raise

read_email_from_gmail()
notification()