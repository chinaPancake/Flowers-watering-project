import sqlite3
from datetime import datetime, date, timedelta

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

connect = sqlite3.connect('flowers.db')
c = connect.cursor()
c.execute('''SELECT * FROM flowers''')
records = c.fetchall()
connect.commit()

def new_flower():
    f_name = input('Flower name: ')
    f_description = input('Flower description: ')
    f_frequency = input('Frequency of watering: ')
    f_amount = input('Amount of water to watering in ml: ')
    f_last_watering = input('When was the last watering?(format of input yyyy-mm-dd): ')
    sql = f""" INSERT INTO flowers
                        (name, description, frequency, amount, last_watering)
                        VALUES('{f_name}', '{f_description}', '{f_frequency}', '{f_amount}', '{f_last_watering}')"""
    c.execute(sql)
    connect.commit()
    print(f'You add {f_name} to database!')

def delete_flower():
    print('-------------')
    for name in records:
        print('flower name: ', name[0])
    f_delete = input('What flower do you want to delete? (put flower name, if u want to go back put quit): ')
    if f_delete.lower() == 'quit':
        print('-------------')
        pass
    elif f_delete.lower() != 'quit':
        c.execute(f"""DELETE FROM flowers WHERE name LIKE '{f_delete}'""")
        print(f'You just delete {f_delete}')
        connect.commit()
        print('-------------')

def show_flowers():
    print('-------------')
    for row in records:
        print("Name: ", row[0])
        print("Description: ", row[1])
        print("once_every: ", row[2])
        print("How_much in ml: ", row[3])
        print('Last watering: ', row[4])
        print('-------------')

def next_watering():
    from datetime import date
    print('-------------')
    print('Today is: ', date.today())
    print('-------------')
    for date in records:
        dateint = datetime.strptime(date[4], '%Y-%m-%d')
        timedelta_dateint = dateint + timedelta(days=date[2])
        print('Last watering of ', date[0], f'(water every {date[2]} days)', ' was', date[4],
              'Next watering should be done in ', timedelta_dateint.strftime("%Y-%m-%d"))
    print('-------------')

def save_to_file():
    print('Save to file')
    with open('share.txt', 'w', encoding='utf-8') as save_to_file:
        for save in records:
            dateint = datetime.strptime(save[4], '%Y-%m-%d')
            timedelta_dateint = dateint + timedelta(days=save[2])
            save_to_file.write(f'Flower name: {save[0]} \n'),
            save_to_file.write(f'Flower Description:  {save[1]} \n'),
            save_to_file.write(f'Flower Once_every:  {save[2]} \n'),
            save_to_file.write(f'Flower How Much water:  {save[3]} \n'),
            save_to_file.write(f'Flower Last Watering:  {save[4]} \n'),
            save_to_file.write(f'Flower Next Watering: {timedelta_dateint.strftime("%Y-%m-%d")}\n')
            save_to_file.write('\n ------------------ \n\n'),

menu_options= {
    1: '1. Add new flower',
    2: '2. Delete flower from database',
    3: '3. Show info about all flowers',
    4: '4. When next watering',
    5: '5. Save to file',
    6: '6. Exit',
}

while(True):
    print_menu()
    option = int(input('Chose menu option: '))
    if option == 1:
        new_flower()
    elif option == 2:
        delete_flower()
    elif option == 3:
        show_flowers()
    elif option == 4:
        next_watering()
    elif option == 5:
        save_to_file()
    elif option == 6:
        print("Thanks for today! Let's grow togheter! ")
        connect.commit()
        exit()
