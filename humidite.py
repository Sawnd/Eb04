import database
import json
import html
import cgi

query2='SELECT * FROM humidite ORDER BY Date LIMIT 20'
database.cursor.execute(query2)
results2 = database.cursor.fetchall()

data = {}
data["humidite"] = []
for h in results2:
    hum = {}
    #hum[h['Valeur']]= h['Date'].strftime('%d/%m/%Y %H:%M')
    hum[h['Valeur']] = h['ID']
    data["humidite"].append(hum)

print(html.header)
print(json.dumps(data, indent=6))
print(html.footer)