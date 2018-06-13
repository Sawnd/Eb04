import database
import json
import html

query1='SELECT * FROM temperature ORDER BY Heure LIMIT 20'
database.cursor.execute(query1)
results1 = database.cursor.fetchall()

data = {}
data["temperature"] = []
for t in results1:
    temp = {}
    temp[t['Valeur']]=t['Heure'].strftime('%d/%m/%Y %H:%M')
    data["temperature"].append(temp)

print("""
    """)
#print(html.header)
print(json.dumps(data, indent=6))


