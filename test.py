from HTU21D import HTU21D
import database

temperature = HTU21D(1).read_temperature()

database.cursor.execute("INSERT INTO Temperature  VALUES ('','NOW()',t)")