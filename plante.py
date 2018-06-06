import cgi
import plotly
import cgitb
import database
cgitb.enable()

#On récupère dans la base de données toutes les données de la table 'temperature'
query='SELECT * FROM temperature ORDER BY Heure'
database.cursor.execute(query)
results = database.cursor.fetchall()



html2 = """"
<head>
    <title>Ajouter une plante</title>
</head>
<body>
<form action='plante.py' method='post'>
            <label for='nom'>Nom:</label><input type="text" required id ='nom' name='nom'><br>
            <label for='temperature'>Temp&eacuterature optimale:</label><input type='text' id='temperature'><br>
            <label for='humidite'>Humidit&eacute optimale:</label><input type='text' id='humidite' name="humidite"><br>
            <label for='ensoleillement'>Ensoleillement optimal:</label><input type='text' name="ensoleillement" id='ensoleillement'><br>
            <input type="submit" value="Ajouter">
        </form>
    
"""

print("Content-type: text/html; charset=utf-8\n")
html2 += """</body>
</html>"""

planteForm = cgi.FieldStorage()
nom = planteForm.getvalue('nom')
temperature = planteForm.getvalue('temperature')
humidite =planteForm.getvalue('humidite')
ensoleillement = planteForm.getvalue('ensoleillement')
database.cursor.execute("INSERT INTO plante (Nom,Temperature,Humidite,Ensoleillement) VALUES ('%s','%d','%d','%d')"
                        % nom, temperature, humidite, ensoleillement)


print(html2)

