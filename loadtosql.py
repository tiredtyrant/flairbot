import sqlite3 as sqlite

con = sqlite.connect('estados_municipios.db')
cur = con.cursor()

script = open('estados_municipios.sql','r',encoding='utf-8').read()

cur.executescript(script)