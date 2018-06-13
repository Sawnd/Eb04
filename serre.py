
import cgitb
import plante
cgitb.enable()


listePlantes=plante.plantes

formulaireSerre = """


<h1> Cr&eacuteer une serre </h1>
<form class='cf' action='serre.py' method='post'>
            <div class='cf left'>
           <input type="text" required id ='nom' name='nom' placeholder='Nom'><br>
           <input type="text" disabled placeholder='Plante(s)'><br>
           <select id="serre" placeholder='Plante'' ><option=''></option>"""
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