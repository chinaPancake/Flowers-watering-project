import calendar
import sqlite3
import datetime

class Flower():
    def __init__(self, name, once_every, how_much):
        self.name = name
        self.once_every = once_every
        self.how_much = how_much

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect('flowers.db')
    except Error as e:
        print(e)

    return conn

def select_all_task(conn):
    cur = conn.cursor()
    cur.exectue('SELECT * FROM flowers')
    rows = cur.fetchall()

    for row in rows:
        print(row)

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

#All inputs of the flower, prolly later im gonna do it in list of lists so we can get acess to every flower insted of just one
flowers = []
#flower = Flower(name=input('What is the name of the flower: '), once_every=int(input('How many days till another watering: ')), how_much=float(input('How much water in ml: ')))
flower = Flower(name=cur.execute('SELECT name FROM flowers'), once_every=cur.execute('SELECT once_every FROM flowers'), how_much=cur.execute('SELECT how_much FROM flowers'))

flowers.append(flower.name)
flowers.append(flower.once_every)
flowers.append(flower.how_much)

now = datetime.datetime.now()
base = datetime.datetime.today()
print('Today is: ',now.strftime("%A"), ' next watering should be done in: ', base+datetime.timedelta(days=row[2]), f' and you should add {row[3]} ml of water')
print('Last watering was', base-datetime.timedelta(days=row[2]))