import sqlite3

con = sqlite3.connect('TestDB.db')

cur = con.cursor()


for row in cur.execute('SELECT * FROM URL'):
    print(row)
