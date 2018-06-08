import cgi
import cgitb
import database
cgitb.enable()



html2 = """
<head>
    <title>Ajouter une plante</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">    
    <link rel="stylesheet" type="text/css" href="/assets/css/style.css">
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
</head>
<body>
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


print("Content-type: text/html; charset=utf-8\n")
html2 += liste
html2 += """</body>
</html>"""

planteForm = cgi.FieldStorage()

nom = str(planteForm.getvalue('nom'))
temperature = planteForm.getvalue('temperature')
humidite = planteForm.getvalue('humidite')
ensoleillement = planteForm.getvalue('ensoleillement')
 #On verifie que le formulaire nn'est pas vide
if(nom != 'None'):
    database.cursor.execute("INSERT INTO plante (Nom,Temperature,Humidite,Ensoleillement) VALUES ('{0}','{1}','{2}','{3}')"
                            .format(nom, temperature, humidite, ensoleillement))
    database.db.commit()

print(html2)

