#Librairie pour ajouter des fonctions à utiliser dans différentes pages

import datetime
import http


def convert_date(x,y,z):
    orig_date = datetime.datetime(x,y,z)
    orig_date = str(orig_date)
    d = datetime.datetime.strptime(orig_date, '%Y-%m-%d %H:%M:%S')
    d = d.strftime('%m/%d/%y')
    return d

