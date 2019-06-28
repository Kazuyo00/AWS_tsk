#coding: utf-8

import sqlite3
from contextlib import closing

db = './stocklist.db'

with closing(sqlite3.connect(db)) as con:
  
  cur = con.cursor()

  check_table = cur.execute('select * from stocks')
  print('-*- before -*-')
  print(cur.fetchall())
  print()

  delete_table = 'delete from stocks'
  cur.execute(delete_table)

  check_table = cur.execute('select * from stocks')
  print('-*- after -*-')
  print(cur.fetchall())

  con.commit()

  con.close()
