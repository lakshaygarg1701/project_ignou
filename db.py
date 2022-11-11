import sqlite3
import datetime as dt
from dateutil.parser import parse

conn=sqlite3.connect('db.sqlite3')
cur=conn.cursor()
source="event"
target="event_rep"
cur.execute("select * from event left join event_rep on event.date=event_rep.date where event.date<(?)",(dt.datetime.today().strftime("%Y-%m-%d"),))
rows=cur.fetchall()
for x in rows:
	print(x)
# for x in cur:
# 	if(parse(x[4])<dt.datetime.today()):
# 		rows=cur.fetchall()
# 		for x in rows:
# 			print(x)
conn.commit()
conn.close()