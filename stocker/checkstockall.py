#coding: utf-8

import sqlite3
import sys
from contextlib import closing

#print(sys.argv[1])

db = './stocklist.db'

with closing(sqlite3.connect(db)) as con:
  
    cur = con.cursor()
  
    create_table = 'create table if not exists stocks (name varchar(8), amount int)'
    cur.execute(create_table)
  
    check_table = cur.execute('select * from stocks')
    getlist = cur.fetchall()
    gllist = list(getlist)
    print('-*- before -*-')
    print(list(getlist))
    print()

    getdata = cur.execute('select * from stocks order by name')
    rawdata = getdata.fetchall()             #tupled data
    nameamount = [[x[0], x[1]] for x in rawdata]
    for x in nameamount:
        if x[1] != 0:
            print(x[0]+": "+str(x[1]))
    print()

    check_table = cur.execute('select * from stocks')
    print('-*- after -*-')
    print(cur.fetchall())
  
    con.commit()
  
    con.close()
