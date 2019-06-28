#coding: utf-8

import sqlite3
import sys
from contextlib import closing

#print(sys.argv[1])

sname = sys.argv[1]
samount = sys.argv[2]

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

    getdata = cur.execute('select amount from stocks where name = \"' + sname + '\"')
    oldamount = getdata.fetchall()[0][0]
    nowamount = oldamount - int(samount)
    if nowamount <= 0:
        nowamount = 0

    print("sold... " + sname + ": " + str(nowamount))
    print()
    cur.execute('update stocks set amount = \"'+ str(nowamount) + '\" where name = \"' + sname + '\"')

    check_table = cur.execute('select * from stocks')
    print('-*- after -*-')
    print(cur.fetchall())

    con.commit()

    con.close()
