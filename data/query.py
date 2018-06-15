import database
query2 ='SELECT * FROM plante ORDER BY Nom'

cursor =database.cursor.execute(query2)
plantes = database.cursor.fetchall()
#liste des serres
query3= 'SELECT * FROM serre '
cursor=database.cursor.execute(query3)
liste_serres=database.cursor.fetchall()