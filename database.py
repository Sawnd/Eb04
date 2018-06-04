#!/usr/bin/python

#représente la connexion à la base de données

import pymysql.cursors
# Connect
db = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="eb04")

cursor = db.cursor()

