import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clients (''id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')')

for lin in cursor.fetchall():
    index, name, weight = lin
    print(index, name, weight)

cursor.close()
connection.close()
