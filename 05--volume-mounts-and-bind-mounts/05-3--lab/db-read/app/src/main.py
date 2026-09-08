import sqlite3

import polars as pl

connection = sqlite3.connect('/data/app.db')

df = pl.read_database(
    query="SELECT * FROM users",
    connection=connection,
)

print(df)

connection.close()
