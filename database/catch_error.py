import sqlite3

url_list = [
    ('todayonline.com', 'John Ng'),
    ('cna.com', 'Jack Ong')
]
con = sqlite3.connect('TestDB.db')
cur = con.cursor()

cur.executemany('INSERT INTO CLIENTS VALUES(?,?)',
                url_list)

cur.execute('select * from clients')
print(cur.fetchall())
