
from scipy import misc
from picamera import PiCamera
from time import sleep
import database

def b_measure(image):
    "Mesure de la luminosité relaitve"
    fichier=image+'.jpg'
    img = misc.imread(fichier)
    Y = []
    for i in range(0,len(img)-1):
            Y=[0.2126*img[i][j][0]+0.7152*img[i][j][1]+0.0722*img[i][j][2] for j in range(0,len(img[0])-1)]
    L=sum(Y)/len(Y)
    database.cursor.execute("INSERT INTO Ensoleillement (Valeur) VALUES ('%d') " % L)
    database.db.commit()
    print(L)
    return L;

camera=PiCamera()


camera.start_preview()
sleep(5)
image=camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

b_measure(image)









