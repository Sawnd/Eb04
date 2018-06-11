#!/usr/bin/python

#représente la connexion à la base de données

import pymysql.cursors
# Connexion en local
db = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="eb04",charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
#Connexion sur le raspberry
#db = pymysql.connect(host="89.84.40.210",
                       #user="root",
                       #passwd="pi",
                       #db="eb04",charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

