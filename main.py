import sqlite3
import datetime

class Flower():
    def __init__(self, name, once_every, how_much):
        self.name = name
        self.once_every = once_every
        self.how_much = how_much

conn = sqlite3.connect('flowers.db')
cur = conn.execute('SELECT * FROM flowers')
records = cur.fetchall()

#get all info about flower
for row in records:
     print("Name: ", row[0])
     print("Description: ", row[1])
     print("once_every: ", row[2])
     print("How_Often: ", row[3])
     print("\n")

#flower = Flower(name=input('What is the name of the flower: '), once_every=int(input('How many days till another watering: ')), how_much=float(input('How much water in ml: ')))
flower = Flower(name=cur.execute('SELECT name FROM flowers'), once_every=cur.execute('SELECT once_every FROM flowers'), how_much=cur.execute('SELECT how_much FROM flowers'))

#Dates
now = datetime.datetime.now().date()
base = datetime.datetime.today().date()
next_watering = base + datetime.timedelta(days=row[2])
last_watering = base - datetime.timedelta(days=row[2])

print('Today is: ',now.strftime("%A"), f'({now})', ' next watering should be done in: ', next_watering.strftime("%A"), f'({next_watering})' , f' and you should add {row[3]} ml of water')
print('Last watering was', last_watering.strftime("%A") ,f'({last_watering})')