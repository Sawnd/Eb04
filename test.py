#from HTU21D import HTU21D
import datetime
import database
import schedule
import time


def job():
    temperature = 35
    database.cursor.execute("INSERT INTO Temperature (Valeur) VALUES ('%d') " % temperature)
    database.db.commit()
    print(temperature)


schedule.every(10).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)


#On récupère la  température et on l'enregistre dans la base de données
#timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#temperature = HTU21D(1).read_temperature()



