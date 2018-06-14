header = """<html>
    Content-type: text/html; charset=utf-8\n
    <head>
    <title>Surveillance de serre</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">    
    <link rel="stylesheet" type="text/css" href="/assets/css/style.css">
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
</head><body><div id="chartContainer" style="height: 370px; width: 100%;"></div>"""

footer = """<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script src="/assets/scripts/script.js"></script>
</body></html>"""

formulairePlante="""

<div id='plante'>
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
    </div>
"""
formulaireSerre = """

<div id='serre'>
<h1> Créer une serre </h1>
<form class='cf' action='serre.py' method='post'>
            <div class='cf left'>
           <input type="text" required id ='nom' name='nom' placeholder='Nom'><br>
           <select id="serre">
           
           </select>
            <input type='text' id='temperature' placeholder='Temperature'><br>
            <input type='text' id='humidite' name="humidite" placeholder='Humidit&eacute'><br>
            <input type='text' name="ensoleillement" id='ensoleillement' placeholder='Ensoleillement optimal'><br>
            <input type="submit" value="Ajouter">
            </div>
        </form>
</div>
"""

redirection = """
<html>
<head>
<title>Redirection...</title>
 
<meta http-equiv="refresh" content="2; URL=/html/accueil.html">
</head>
 
<body>
</body>
 
</html>"""
