import json, string
from aiogram import types
from create_bot import Dispatcher
from aiogram.dispatcher.filters import Text


async def echo_send(message: types.Message):
    await message.reply(f'И тебе привет, {message.from_user.first_name}!')


async def echo_mat(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply(f'Маты запрещены, {message.from_user.first_name}')
        await message.delete()


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send, Text(equals='Привет', ignore_case=True))
    dp.register_message_handler(echo_mat)
