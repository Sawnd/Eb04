import cgi
import cgitb
import plante
import database
cgitb.enable()


listePlantes=plante.plantes

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
html2=formulaireSerre

# Traitement du formulaire
serreForm = cgi.FieldStorage()
nom = str(serreForm.getvalue('nom-serre'))
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
                database.cursor.execute("INSERT INTO serre (ID, Nom) VALUES ('{0},{1}')".format(IDSerre,nom))
                database.db.commit()

print(html2)
