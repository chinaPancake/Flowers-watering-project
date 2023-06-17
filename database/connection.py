import sqlite3


def create_databasE():
    con = sqlite3.connect("../flowers.db")
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE flowers
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(20) NOT NULL,
            description varchar(200),
            frequency integer,
            amount integer,
            last_watering DATE)
            """
    )
    con.commit()
    cur.close()


def add_flower(flower: dict):
    con = sqlite3.connect("flowers.db")
    cur = con.cursor()
    cur.execute(
        """insert into flowers(name, description, frequency, amount, last_watering) values(?,?,?,?,?)""",
        (
            flower["name"],
            flower["description"],
            flower["frequency"],
            flower["amount"],
            flower["last_watering"],
        ),
    )
    con.commit()


def dict_from_row(rows):
    return dict(zip(rows.keys(), rows))


def fet_flower(id):
    con = sqlite3.connect("flowers.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from flowers")
    res = cur.fetchall()
    con.commit()
    return dict(res[id])


def delete_flower(id: int):
    con = sqlite3.connect("flowers.db")
    cur = con.cursor()
    cur.execute(f"delete from flowers where id = '{id}'")
    con.commit()


# print(delete_flower(id=2))
