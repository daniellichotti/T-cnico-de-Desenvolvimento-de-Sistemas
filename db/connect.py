import sqlite3

conn = sqlite3.connect('meubanco.db')

cursor = conn.execute('SELECT * FROM usuarios;')
usuarios = cursor.fetchall()

print(usuarios[0][2])

conn.close()