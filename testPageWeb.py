import cgi
import cgitb
import database
cgitb.enable()

query='SELECT * FROM temperature ORDER BY Heure'
database.cursor.execute(query)
results = database.cursor.fetchall()
html2 = """"<DOCTYPE Html>
<head>
    <title>Résultats</title>
</head>
<body>"""
for data in results:
    html2 += str(data['Valeur']) + "°  " + data['Heure'].strftime('%d/%m/%Y')
    html2 +='<br>'


form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
html2 += """</body>
</html>"""

print(html2)

