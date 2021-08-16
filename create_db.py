import sqlite3

conn = sqlite3.connect('TestDB.db')

c = conn.cursor()

c.execute('''CREATE TABLE URL
             ([Address] text unique)''')

conn.commit()
