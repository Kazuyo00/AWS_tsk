#coding: utf-8

import sqlite3
import sys
from contextlib import closing

print('-*- input -*-')
print(sys.argv[1] + ', ' + sys.argv[2])
print()

sname = sys.argv[1]
samount = sys.argv[2]

db = './stocklist.db'

with closing(sqlite3.connect(db)) as con:
  
    cur = con.cursor()
  
    create_table = 'create table if not exists stocks (name varchar(8), amount int)'
    cur.execute(create_table)
  
    check_table = cur.execute('select * from stocks')
    print('-*- before -*-')
    print(list(cur.fetchall()))
    print()

 
    # check existing or not. prepare for judgement: add or update.
    search = cur.execute('select amount from stocks where name = \"' +sname+ '\"')
    checkamount = search.fetchall()[0][0]

    # add new stock
    if checkamount == []:
        sql = 'insert into stocks (name, amount) values (?, ?)'
        stock = (sname, samount)
        cur.execute(sql, stock)

    # update amount
    else:
        nowamount = checkamount + int(samount)
        cur.execute('update stocks set amount = \"' + str(nowamount) + '\" where name = \"' + sname + '\"')

    check_table = cur.execute('select * from stocks')
    print('-*- after -*-')
    print(list(cur.fetchall()))

    con.commit()

    con.close()
