import cgi
import cgitb
from data import query
import html
import database
cgitb.enable()

html2 = html.header
listePlantes=query.plantes

formulaireSerre = """
<div id='serre'>

<h1> Cr&eacuteer une serre </h1>
<form class='cf' action='serre.py' method='post'>
            <div class='cf left'>
           <input type="text" required id ='nom-serre' name='nom-serre' placeholder='Nom'><br>
           <input type="text" disabled placeholder='Plante(s)'><br>
           <select id="select-serre" name='select-serre' multiple ><option=''></option>"""
for p in listePlantes:
    formulaireSerre += "<option value ='" + str(p["ID"]) + "'>" + p["Nom"] +"</option>"
formulaireSerre += """
           </select>
            <input type="submit" value="Ajouter">
            </div>
        </form>
</div>
"""
html2 += formulaireSerre

# Traitement du formulaire

serreForm = cgi.FieldStorage()
nom = str(serreForm.getvalue('nom-serre'))
html2 += nom
select = serreForm.getvalue('select-serre')

 #On verifie que le formulaire n'est pas vide
if nom != 'None':
    database.cursor.execute("INSERT INTO serre (Nom)"
                            " VALUES ('{0}')".format(nom))

    database.db.commit()
    #On récupère l'ID que l'on vient d'insérer
    database.cursor.execute("SELECT * FROM serre ORDER BY ID DESC  LIMIT 1")
    results= database.cursor.fetchone()
    if results:
        IDSerre = int(results['ID'])
        if select:
            for plante in select:
                database.cursor.execute("INSERT INTO serre_plante (IDSerre, IDPlante) VALUES ('{0}','{1}')".format(IDSerre,plante))
                database.db.commit()
html2 += html.footer

#On affiche les serres
listeSerres=query.liste_serres
htmlSerre="""<div id='serres'><h1>Mes serres</h1>"""
for serre in listeSerres:
    ID_serre = serre['ID']
    htmlSerre += "<h2>"+serre['Nom']+"""</h2><br><table class='pure-table center ' style="
    margin:  auto;"
><thead><th>Plante</th><th>Temperature</th><th>Humidite</th><th>Ensoleillement</th></thead>
<tbody>"""
    database.cursor.execute("SELECT serre.Nom AS serre,plante.Nom As plante, plante.Temperature,plante.Humidite,plante.Ensoleillement  FROM serre_plante INNER JOIN plante on serre_plante.IDPlante = plante.ID INNER JOIN serre ON serre_plante.IDSerre = serre.ID WHERE IDSerre='{0}' ".format(ID_serre))
    listePlantes_serres = database.cursor.fetchall()
    for plante_serre in listePlantes_serres:
        htmlSerre += "<tr><td>" +str(plante_serre['plante']) + "</td><td>"+ str(plante_serre['Temperature']) + "</td><td>" + \
                 str(plante_serre['Humidite']) + "</td><td>" + str(plante_serre["Ensoleillement"]) + "</td></tr>"
    htmlSerre +="""</tbody></table>"""

html2+=htmlSerre






print(html2)
