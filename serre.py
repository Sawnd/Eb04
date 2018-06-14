import cgi
import cgitb
import plante
import database
cgitb.enable()


listePlantes=plante.plantes

formulaireSerre = """


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

"""
html2=formulaireSerre
print(html2)
# Traitement du formulaire
serreForm = cgi.FieldStorage()
nom = str(serreForm.getvalue('nom-serre'))
select = serreForm.getvalue('select-serre')

 #On verifie que le formulaire n'est pas vide
if nom != 'None':
    database.cursor.execute("INSERT INTO serre (Nom)"
                            " VALUES ('{0}','{1}','{2}','{3}')".format(nom, temperature, humidite, ensoleillement))
    database.db.commit()
