import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('movies.db')


c = conn.cursor()

c.execute("DROP TABLE movies") 

c.execute("""CREATE TABLE movies( 
	movie_name text,
	lead_actor text,
	actress text,
	year_of_release integer,
	director_name text
	)""")

c.execute("INSERT INTO movies VALUES('Interstellar' ,'Matthew McConaughey','Anne Hathaway','2014','Christopher Nolan')")
c.execute("INSERT INTO movies VALUES('Pacific Rim' ,' Charlie Hunnam','Rinko Kikuchi','2013','Guillermo del Toro')")
c.execute("INSERT INTO movies VALUES('Charlie and the Chocolate Factory','Johnny Depp','hehe','2005','Tim Burton')")
c.execute("INSERT INTO movies VALUES('Pirates of the Caribbean ','Johnny Depp','Keira Knightely','2003','Gore Verbinski')")

c.execute("SELECT * FROM movies ")



rows = c.fetchall()

for row in rows:
	print(row)
print("")
c.execute("SELECT * from movies WHERE lead_actor = 'Johnny Depp'") 
  

rows = c.fetchall()

for row in rows:
	print(row)

	

conn.commit()

conn.close()
