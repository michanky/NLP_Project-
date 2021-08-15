import sqlite3

con = sqlite3.connect('TestDB.db')

cur = con.cursor()

cur.execute('''INSERT INTO CLIENTS VALUES 
            ("www.straitstimes.com",
            "Michael Ng")''')

con.commit()

print('Inserted one entry')

for row in cur.execute('SELECT * FROM CLIENTS'):
    print(row)
