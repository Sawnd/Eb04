import cgi
import cgitb
import database
cgitb.enable()



html2 = """
<head>
    <title>Ajouter une plante</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">    
    <link rel="stylesheet" type="text/css" href="/assets/css/style.css">
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

