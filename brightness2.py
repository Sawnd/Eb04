# coding=utf-8
from scipy import misc
from picamera import PiCamera
from time import sleep
import ImageStat
import os
import Image
import  database
import datetime

def m():
	im=Image.open('/root/test_xeno/projet/image.jpg').convert('L')
	stat=ImageStat.Stat(im)
	e=stat.rms[0]
	b=e*100/255
	print(b)
	return b

camera=PiCamera()
sleep(5)
image=camera.capture('/root/test_xeno/projet/image.jpg')
br=m()
os.remove('/root/test_xeno/projet/image.jpg')	 

database.cursor.execute("INSERT into ensoleillement (Valeur) values('%d')"%br)
database.db.commit()
