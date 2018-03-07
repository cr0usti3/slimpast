#!/usr/bin/env python3


from bottle import Bottle,request
import sqlite3
import datetime
import time
import random
from string import hexdigits

app=Bottle()


def wbd():

  conn=sqlite3.connect('app.db')
  s=conn.cursor()
  s.execute('CREATE TABLE if not exists  data(date text,id text,content text)')
  return conn

def genurl():
  r=random.choice(hexdigits)
  for x in range(10):
    r=random.choice(hexdigits)+r
  return r

@app.post('/',method=['get','post'])
def index():

  content=request.forms.get('postdata')
  print(request.url)
  #print(request.environ)
  # print(request.get_header)
  if content :
    now=datetime.datetime.now()
    timestamp=time.mktime(now.timetuple())
    conn=wbd()
    s=conn.cursor()
    s.execute("INSERT INTO data values({},'url gen','{}');".format(timestamp,content))
    conn.commit()
    conn.close()
    return (content)
  else :
    return('hello no postdata')


if __name__ == '__main__':
  app.run(host='localhost',port='8000',debug=True)



