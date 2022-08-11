import sqlite3
import datetime

class Flower:
    def __init__(self, name, description, frequency, amount, last_watering):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.amount = amount
        self.last_watering = last_watering

def print_menu():
    for key in menu_options.keys():
        print(menu_options[key])

menu_options= {
    1: '1. Add new flower',
    2: '2. Delete flower from database',
    3: '3. Show info about all flowers',
    4: '4. Exit',
}
# connect with database
conn = sqlite3.connect('flowers.db')
cur = conn.cursor()
cur = conn.execute('SELECT * FROM flowers')
records = cur.fetchall()
conn.commit()

while(True):
    print_menu()
    option = int(input('Select from menu: '))

    if option == 1:
        f_name = input('Flower name: ')
        f_description = input('Flower description: ')
        f_frequency = input('Frequency of watering: ')
        f_amount = input('Amount of water to watering in ml: ')
        f_last_watering = input('When was the last watering?(format of input yyyy-mm-dd): ')
        # insert new flower into database
        sql = f""" INSERT INTO flowers
                    (name, description, once_every, how_much, last_watering)
                    VALUES('{f_name}', '{f_description}', '{f_frequency}', '{f_amount}', '{f_last_watering}')"""
        sql_execute = conn.execute(sql)
        conn.commit()
        print('Insert operation ok! ')

    # Delete from database
    elif option == 2:
        print('-------------')
        for name in records:
            print('flower name: ', name[0])
        f_delete = input('What flower do you want to delete? (put flower name): ')
        if f_delete.lower() == 'quit':
            print('-------------')
            pass
        elif f_delete.lower() != 'quit':
            cur.execute(f"""DELETE FROM flowers WHERE name LIKE '{f_delete}'""")
            conn.commit()
            print(f'You just delete {f_delete}')
            print('-------------')

    # get all info about flower
    elif option == 3:
        print('-------------')
        for row in records:
            print("Name: ", row[0])
            print("Description: ", row[1])
            print("once_every: ", row[2])
            print("How_much in ml: ", row[3])
            print('Last watering: ', row[4])
            print('-------------')

    elif option == 4:
        print("Thanks for today! Let's grow togheter! ")
        conn.commit()
        exit()


'''#get data to class, and create object flower from class Flower
flower = Flower(name=row[0], description=row[1], frequency=row[2], amount=row[3], last_watering=row[4])
Dates
now = datetime.datetime.now().date()
base = datetime.datetime.today().date()
next_watering = base + datetime.timedelta(days=row[2])
last_watering = base - datetime.timedelta(days=row[2])
print('Today is: ',now.strftime("%A"), f'({now})', ' next watering should be done in: ', next_watering.strftime("%A"), f'({next_watering})' , f' and you should add {row[3]} ml of water')
print('Last watering was', last_watering.strftime("%A") ,f'({last_watering})')'''
