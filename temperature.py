import database
import json
import html

query1='SELECT * FROM temperature WHERE DATEDIFF(NOW(),Heure) = 0 ORDER BY Heure ASC limit 100'

database.cursor.execute(query1)
results1 = database.cursor.fetchall()

data = {}
data["temperatures"] = []
for t in results1:
    temp = {}
    temp['valeur']=t['Valeur']
    temp['temps']=t['Heure'].strftime('%Y-%m-%dT%H:%M:%S')
    data["temperatures"].append(temp)

print("""
    """)
#print(html.header)
print(json.dumps(data, indent=6))


