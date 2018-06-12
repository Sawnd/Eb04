import database
import json

query1='SELECT * FROM temperature ORDER BY Heure LIMIT 20'
query2='SELECT * FROM humidite ORDER BY Date LIMIT 20'
database.cursor.execute(query1)
results1 = database.cursor.fetchall()
database.cursor.execute(query2)
results2 = database.cursor.fetchall()

data = {}
data["temperature"] = []
data["humidite"] = []
for t in results1:
    temp = {}
    temp[t['Valeur']]=t['Heure'].strftime('%d/%m/%Y %H:%M')
    data["temperature"].append(temp)
for h in results2:
    hum = {}
    hum[h['Valeur']]= h['Date'].strftime('%d/%m/%Y %H:%M')
    data["humidite"].append(temp)
print(json.dumps(data, indent=4))