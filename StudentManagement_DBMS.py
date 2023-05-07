import sqlite3 as sql

db = sql.connect('std.db')
data = db.execute("select * from std")
print(data.fetchall())
