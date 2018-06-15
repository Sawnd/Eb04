import cgi
import cgitb
import database
import html
cgitb.enable()


html2 = html.header
html2 += html.formulairePlante

# Tableaux contenant la liste des plantes
query2 ='SELECT * FROM plante ORDER BY Nom'

cursor =database.cursor.execute(query2)
plantes = database.cursor.fetchall()
liste = html.listePlanteHaut
for p in plantes:
    liste += "<tr><td>" + str(p['Nom']) + "</td><td>" + str(p['Temperature']) + "</td><td>" +\
             str(p['Humidite']) + "</td><td>" + str(p["Ensoleillement"]) + "</td></tr>"
liste += html.listePlanteBas
html2 += liste
html2 += """</body>
</html>""" + html.footer
# Traitement du formulaire
planteForm = cgi.FieldStorage()
nom = str(planteForm.getvalue('nom'))
temperature = planteForm.getvalue('temperature')
humidite = planteForm.getvalue('humidite')
ensoleillement = planteForm.getvalue('ensoleillement')
 #On verifie que le formulaire n'est pas vide
if nom != 'None':
    database.cursor.execute("INSERT INTO plante (Nom,Temperature,Humidite,Ensoleillement)"
                            " VALUES ('{0}','{1}','{2}','{3}')".format(nom,temperature, humidite, ensoleillement))
    database.db.commit()


print(html2)

