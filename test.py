#from HTU21D import HTU21D
import database
import schedule
import time
import random


def job():
    temperature = random.randint(-10,90)
    humidite = random.randint(0,100)
    ensoleillement = random.randint(0,100)
    database.cursor.execute("INSERT INTO temperature (Valeur) VALUES ('%d') " % temperature)
    database.db.commit()
    print("temperature")
    print(temperature)

    database.cursor.execute("INSERT INTO humidite (Valeur) VALUES ('%d') " % humidite)
    database.db.commit()
    print("humidite")
    print(humidite)
    database.cursor.execute("INSERT INTO ensoleillement (Valeur) VALUES ('%d') " %ensoleillement)
    database.db.commit()
    print("ensoleillement")
    print(ensoleillement)

def job2():
    database.cursor.execute("TRUNCATE TABLE ensoleillement")
    database.db.commit()
    database.cursor.execute("TRUNCATE TABLE humidite")
    database.db.commit()
    database.cursor.execute("TRUNCATE TABLE temperature")
    database.db.commit()
    print("tables vidéees");

schedule.every(3).seconds.do(job)
schedule.every(5).minutes.do(job2)
while 1:
    schedule.run_pending()
    time.sleep(1)


#On récupère la  température et on l'enregistre dans la base de données
#timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#temperature = HTU21D(1).read_temperature()



