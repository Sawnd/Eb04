import database
import json
import http.server
import html

query1 = 'SELECT * FROM temperature WHERE DATEDIFF(NOW(),Heure) = 0 ORDER BY Heure DESC limit 100'
query2 = 'SELECT * FROM humidite WHERE DATEDIFF(NOW(),Date) = 0 ORDER BY Date DESC limit 100'
query3=  'SELECT * FROM ensoleillement WHERE DATEDIFF(NOW(),Date = 0 ORDER BY Date DESC limit 100)'

database.cursor.execute(query1)
results1 = database.cursor.fetchall()
database.cursor.execute(query2)
results2 = database.cursor.fetchall()
database.cursor.execute(query3)
results3=database.cursor.fetchall()

data = {}
data["temperatures"] = []
data["humidites"]= []
for t in results1:
    temp = {}
    temp['valeur'] = t['Valeur']
    temp['temps'] = t['Heure'].strftime('%Y-%m-%dT%H:%M:%S')
    data["temperatures"].append(temp)
for h in results2:
    hum = {}
    hum['valeur'] = h['Valeur']
    hum['temps'] = h['Date'].strftime('%Y-%m-%dT%H:%M:%S')
    data["humidites"].append(hum)

for e in results3:
    ens = {}
    ens['valeur'] = e['Valeur']
    ens['temps'] = e['Date'].strftime('%Y-%m-%dT%H:%M:%S')
    data["ensoleillement"].append(ens)

print("""
    """)
#print(html.header)
print(json.dumps(data, indent=6))

