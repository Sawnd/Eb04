# coding=utf-8
from scipy import misc
from picamera import PiCamera
from time import sleep
import ImageStat
import os
import Image
import  database
import datetime

uri ='/root/test_xeno/projet/'
image ='image.jpg'
uri+=image
def m():
	im=Image.open(uri).convert('L')
	stat=ImageStat.Stat(im)
	e=stat.rms[0]
	b=e*100/255
	print(b)
	return b

camera=PiCamera()
sleep(5)
image=camera.capture(uri)
br=m()
os.remove(uri)

database.cursor.execute("INSERT into ensoleillement (Valeur) values('%d')"%br)
database.db.commit()
