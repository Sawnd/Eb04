header = """<html>
    Content-type: text/html; charset=utf-8\n
    <head>
    <meta charset="UTF-8">
    <title>Surveillance de serre</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">    
    <link rel="stylesheet" type="text/css" href="/assets/css/style.css">
    <link rel="stylesheet" href="/assets/css/multi.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="/assets/scripts/multi.js"></script>

    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
</head><body><div id="chartContainer" style="height: 370px; width: 100%;"></div>

<div id='data'>
    <input type='text' value='' id='value-temperature' disabled hidden>
    <input type='text' value='' id='value-humidite' disabled hidden>
    <input type='text'  disable id='value-ensoleillement' disabled hidden>
</div>"""

footer = """
<nav class="navbar navbar-inverse navbar-fixed-bottom">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Surveillance de serre</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="serre.py">Mes serres</a></li>
      <li><a href="plante.py">Mes plantes</a></li>
    </ul>
  </div>
</nav>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script src="/assets/scripts/script.js"></script>
<br><br><br><br>
</body></html>"""

formulairePlante="""

<div id='plante'>
<h1> Ajouter une plante </h1>
<form class='cf' action='plante.py' method='post'>
            <div class='cf left'>
           <input type="text" required id ='nom' name='nom' placeholder='Nom'><br>
            <input type='text' id='temperature' name='temperature' placeholder='Temperature'><br>
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
listePlanteHaut="""
<div id='liste-plantes'>
<h1>Liste de plantes</h1>
<table class='pure-table center ' style="
    margin:  auto;"
><thead><th>Plante</th><th>Temperature</th><th>Humidite</th><th>Ensoleillement</th></thead>
<tbody>"""

listePlanteBas=""" </tbody>
</table>
</div>

"""

