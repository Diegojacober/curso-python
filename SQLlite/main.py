import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()


# SQL
cursor.execute(
    f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
        );"""
)
con.commit()

# LIMPAR TABELA:

cursor.execute(
    f'DELETE FROM "{TABLE_NAME}";'
)

# Bind normal
# sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)"

# cursor.execute(sql, ['Diego', '10'])

# cursor.executemany(sql, (['Diego', '60'], ['Carlos', 60]))


#Bind com dicionário
sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (:nome, :peso)"

# cursor.execute(sql, {'nome': 'Diego', 'peso': 50})

cursor.executemany(sql, ({'nome': 'Diego', 'peso': 50}, {'nome': 'Roberto', 'peso': 80}))

con.commit()



cursor.close()
con.close()
