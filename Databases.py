import sqlite3

con = sqlite3.connect('./workshop.db')
cur = con.cursor()

cur.execute("CREATE TABLE movies(title, year, rating)")

cur.execute("""
    INSERT INTO movies VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

cur.execute("SELECT title FROM movies")
print(cur.fetchall())

# con.commit()