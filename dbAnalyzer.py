import sqlite3
con = sqlite3.connect("Records.db")
cur = con.cursor()

# Define the SQL statement to select all rows from the table
sql = '''SELECT distinct * FROM MisaLevels order by timestamp desc'''

# Execute the SQL statement
cur.execute(sql)

# Fetch all the rows returned by the SQL statement
rows = cur.fetchall()

# Print the rows
for row in rows:
    print(row)
