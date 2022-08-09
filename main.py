import sqlite3
import datetime

class Flower():
    def __init__(self, name, description, once_every, how_much, last_watering):
        self.name = name
        self.description = description
        self.once_every = once_every
        self.how_much = how_much
        self.last_watering = last_watering

f_name = input('Flower name: ')
f_description = input('Flower description: ')
f_once_every = input('Once every day in a week, this plant need watering: ')
f_how_much = input('How much water in ml does this flower need: ')
f_last_watering = input('When was the last watering?(format of input yyyy-mm-dd): ')

# connect with database
conn = sqlite3.connect('flowers.db')

# insert new flower into database
sql = f""" INSERT INTO flowers
            (name, description, once_every, how_much, last_watering)
            VALUES('{f_name}', '{f_description}', '{f_once_every}', '{f_how_much}', '{f_last_watering}')"""

cur = conn.cursor()
cur = conn.execute('SELECT * FROM flowers')
bdw = conn.execute(sql)
records = cur.fetchall()
conn.commit()
print('Insert operation ok! ')

#get all info about flower
for row in records:
     print("Name: ", row[0])
     print("Description: ", row[1])
     print("once_every: ", row[2])
     print("How_much in ml: ", row[3])
     print('Last watering: ', row[4])
     print("\n")

#get data to class, and create object flower from class Flower
flower = Flower(name=row[0],description=row[1], once_every=row[2], how_much=row[3], last_watering=row[4])

#Dates
now = datetime.datetime.now().date()
base = datetime.datetime.today().date()
next_watering = base + datetime.timedelta(days=row[2])
last_watering = base - datetime.timedelta(days=row[2])

print('Today is: ',now.strftime("%A"), f'({now})', ' next watering should be done in: ', next_watering.strftime("%A"), f'({next_watering})' , f' and you should add {row[3]} ml of water')
print('Last watering was', last_watering.strftime("%A") ,f'({last_watering})')
