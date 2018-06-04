#from HTU21D import HTU21D
import datetime
import database


#On récupère la  température et on l'enregistre dans al base de données
#timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#temperature = HTU21D(1).read_temperature()
temperature = 35
database.cursor.execute("INSERT INTO Temperature (Valeur) VALUES ('%d') " % temperature)
database.db.commit()

