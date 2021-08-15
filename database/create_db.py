import sqlite3

conn = sqlite3.connect('TestDB.db')

c = conn.cursor()

c.execute('''CREATE TABLE CLIENTS
             ([URL] text unique, 
             [Author] text)''')

conn.commit()
