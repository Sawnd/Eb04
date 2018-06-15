import database
query2 ='SELECT * FROM plante ORDER BY Nom'

cursor =database.cursor.execute(query2)
plantes = database.cursor.fetchall()