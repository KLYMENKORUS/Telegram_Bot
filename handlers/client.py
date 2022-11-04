from aiogram import types
from create_bot import bot, Dispatcher
from keyboards import kb_client
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Здравствуйте, {message.from_user.first_name}',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/route22_bot')


async def open_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')
        # await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/route22_bot')


async def place_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'г.Дружковка, ул.Соборная 50')
        # await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/route22_bot')


async def pizza_menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, Text(equals='Режим работы', ignore_case=True))
    dp.register_message_handler(place_command, Text(equals='Расположение', ignore_case=True))
    dp.register_message_handler(pizza_menu, Text(equals='Меню', ignore_case=True))