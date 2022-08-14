import sqlite3
connect = sqlite3.connect('flowers.db')
c = connect.cursor()
records = c.fetchall()
connect.commit()

create = '''CREATE TABLE flower(
            name TEXT PRIMARY KEY,
            description text,
            frequency int,
            amount int default 250,
            last_watering DATE,
            next_watering DATE)'''
c.execute(create)
connect.commit()