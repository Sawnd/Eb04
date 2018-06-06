#from HTU21D import HTU21D
import datetime
import database
import schedule
import time
import random


def job():
    temperature = random.randint(0,100)
    database.cursor.execute("INSERT INTO Temperature (Valeur) VALUES ('%d') " % temperature)
    database.db.commit()
    print(temperature)


schedule.every(30).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)


#On récupère la  température et on l'enregistre dans la base de données
#timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#temperature = HTU21D(1).read_temperature()



