import sqlite3 as sqlite

con = sqlite.connect('estados_municipios.db')
cur = con.cursor()

script = open('estados_municipios.sql').read()

cur.executescript(script)