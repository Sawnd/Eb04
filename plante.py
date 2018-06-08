import cgi
import cgitb
import database
import html
cgitb.enable()


html2 = html.header
html2 += """


<h1> Ajouter une plante </h1>
<form class='cf' action='plante.py' method='post'>
            <div class='cf left'>
           <input type="text" required id ='nom' name='nom' placeholder='Nom'><br>
            <input type='text' id='temperature' placeholder='Temperature'><br>
            <input type='text' id='humidite' name="humidite" placeholder='Humidit&eacute'><br>
            <input type='text' name="ensoleillement" id='ensoleillement' placeholder='Ensoleillement optimal'><br>
            <input type="submit" value="Ajouter">
            </div>
        </form>
    
"""

# Tableaux contenant la liste des plantes
query2 ='SELECT * FROM plante ORDER BY Nom'

cursor =database.cursor.execute(query2)
plantes = database.cursor.fetchall()
liste = """
<table class='pure-table'><thead><th>Plante</th><th>Temperature</th><th>Humidite</th><th>Ensoleillement</th></thead>
<tbody>"""
for p in plantes:
    liste += "<tr><td>" + str(p['Nom']) + "</td><td>" + str(p['Temperature']) + "</td><td>" +\
             str(p['Humidite']) + "</td><td>" + str(p["Ensoleillement"]) + "</td></tr>"
liste += """</tbody>
</table>
"""
html2 += liste
html2 += """</body>
</html>""" + html.footer

planteForm = cgi.FieldStorage()

nom = str(planteForm.getvalue('nom'))
temperature = planteForm.getvalue('temperature')
humidite = planteForm.getvalue('humidite')
ensoleillement = planteForm.getvalue('ensoleillement')
 #On verifie que le formulaire nn'est pas vide
if nom != 'None':
    database.cursor.execute("INSERT INTO plante (Nom,Temperature,Humidite,Ensoleillement)"
                            " VALUES ('{0}','{1}','{2}','{3}')".format(nom, temperature, humidite, ensoleillement))
    database.db.commit()

print(html2)

