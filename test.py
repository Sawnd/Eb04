#from HTU21D import HTU21D
#import database
import pymysql.cursors
import datetime
db = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="eb04")

cursor = db.cursor()
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#temperature = HTU21D(1).read_temperature()
temperature = 22
query = "INSERT INTO Temperature ('Valeur') VALUES ('?')"
query2 ="SELECT * FROM Temperature"

cursor.execute("INSERT INTO Temperature ('Valeur') VALUES ('%d') " % temperature)
#cursor.execute(query2)
db.commit()
results = cursor.fetchall()
for a in results:
    if a:
        print('True')
    else:
        print('False')


#rows = cursor.fetchall()
#print (rows)
print(results)

