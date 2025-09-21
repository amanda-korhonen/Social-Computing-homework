# Task 1

import sqlite3

import pandas as pd

# import os
# os.system('clear')

DB_File = "database.sqlite"

# opening the database
try: 
    con = sqlite3.connect(DB_File)
    print("SQLite Database connected")
except Exception as e:
    print(f"Failed to load the database '{e}'")

tablenames = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", con)
print(tablenames)

for table in ['comments', 'follows', 'posts', 'reactions', 'users']:
    print(f'\n\ncontents of {table}')
    table = pd.read_sql_query(f"SELECT * FROM {table}", con)
    print(table)
