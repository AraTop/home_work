import sqlite3

def seach(word):
   with sqlite3.connect("netflix.db") as connection:
      cursor = connection.cursor()
      cursor.execute(f'SELECT title , country , release_year , type , description FROM netflix WHERE director != " " AND title = "{word}" ')
                 
      for row  in cursor.fetchall():
         json_format = {
         "title": row[0],
         "country": row[1],
         "release_year": row[2],
         "genre": row[3],
         "description": row[4]
          }
   return json_format

def years(one , two):
   with sqlite3.connect("netflix.db") as connection:
      cursor = connection.cursor()
      cursor.execute(f'SELECT title , release_year FROM netflix WHERE release_year BETWEEN {int(one)} AND {int(two)} LIMIT 100 OFFSET 0')
      
      json_format = []
      for row  in cursor.fetchall():
         json_format.append({"title": row[0],
         "release_year": row[1]})
         
      return json_format

def ratings(key):
   with sqlite3.connect("netflix.db") as connection:
      cursor = connection.cursor()
      cursor.execute(f'SELECT title , rating , description FROM netflix WHERE rating = "{key}" ')
   
      json_format = []
      for row  in cursor.fetchall():
         json_format.append({"title": row[0],
         "rating": row[1], "description": row[2]})
         
      return json_format

def genre(genre):
   with sqlite3.connect("netflix.db") as connection:
      cursor = connection.cursor()
      cursor.execute(f'SELECT title , description FROM netflix WHERE type = "{genre}" ORDER BY release_year DESC LIMIT 10 ')

      json_format = []
      for row  in cursor.fetchall():
         json_format.append([{
	      "title": row[0],
	      "description":row[1]
         }])
      return json_format

def cast(name_one, name_two):
   with sqlite3.connect("netflix.db") as connection:
      cursor = connection.cursor()
      cursor.execute(f'SELECT title , release_year , "cast" FROM netflix WHERE "cast" LIKE "%{name_one}%" AND "cast" LIKE "%{name_two}%" AND "cast" > 2 ')

      json_format = []
      for row  in cursor.fetchall():
         json_format.append({"title": row[0], "release_year": row[1],
         "cast": row[2]})

      return json_format

def types_picture(types, year, genre):
   with sqlite3.connect("netflix.db") as connection:
      cursor = connection.cursor()
      cursor.execute(f'SELECT type , release_year , duration_type , title FROM netflix WHERE type = "{types}" AND release_year = "{int(year)}" AND duration_type = "{genre}" ')

      json_format = []
      for row  in cursor.fetchall():
         json_format.append({"title": row[3], "type": row[0],
         "release_year": row[1], "duration_type": row[2]})
   
         return json_format

