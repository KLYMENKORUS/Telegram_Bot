import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('pizza_rout.db')
    cur = base.cursor()
    if base:
        print('Data base connected is OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for read in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, read[0], f'{read[1]}\nОписание: {read[2]}\nЦена: {read[-1]}')


async def sql_read_1():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete(data):
    cur.execute('DELETE  FROM menu WHERE name == ?', (data,))
    base.commit()
