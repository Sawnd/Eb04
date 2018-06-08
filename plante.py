import cgi
import cgitb
import database
cgitb.enable()



html2 = """
<head>
    <title>Ajouter une plante</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">    
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

nom = str(planteForm.getvalue('nom'))
temperature = planteForm.getvalue('temperature')
humidite = planteForm.getvalue('humidite')
ensoleillement = planteForm.getvalue('ensoleillement')
database.cursor.execute("INSERT INTO plante (Nom,Temperature,Humidite,Ensoleillement) VALUES ('{0}','{1}','{2}','{3}')"
                        .format(nom, temperature, humidite, ensoleillement))
database.db.commit()

print(html2)

